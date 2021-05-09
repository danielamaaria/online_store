from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from store.forms import BookForm, OrderContactForm
from store.models import Book, Category, BookOrder, Cart, OrderContact, Order


def index(request):
    context = {
        'header': ''
    }
    return render(request, 'store/index.html', context)


def cart(request):
    try:
        cart_obj = Cart.objects.get(owner=request.user)
    except ObjectDoesNotExist:
        Cart.objects.create(owner=request.user)
        cart_obj = Cart.objects.get(owner=request.user)

    context = {
        "cart": cart_obj
    }
    return render(request, 'store/cart.html', context)


def books(request):
    """Show all available books."""

    book_list: [] = Book.objects.all().order_by('date_added')
    category_list: [] = Category.objects.all()

    context = {
        "books": book_list,
        "categories": category_list
    }
    return render(request, 'store/books.html', context)


def add_to_order(request, book_id):
    cart_obj = Cart.objects.get(owner=request.user)
    quantity = int(request.POST['quantity'])

    # Increment the quantity for existing book in cart.
    for book_order in cart_obj.book_orders.all():
        if book_order.book.id == book_id:
            book_order.quantity = book_order.quantity + quantity
            book_order.save()
            return

    # Create new book order and add it to cart.
    book = Book.objects.get(pk=book_id)
    book_order = BookOrder.objects.create(book=book, quantity=quantity)
    cart_obj.book_orders.add(book_order)


@login_required
def buy_book(request, book_id):
    """
    Create new cart if there isn't one created yet.
    If there is a cart, add the book to it's list of book id's.
    :param quantity:
    :param request:
    :param book_id:
    :return: Redirects to books screen
    """

    try:
        add_to_order(request, book_id)
    except ObjectDoesNotExist:
        Cart.objects.create(owner=request.user)
        add_to_order(request, book_id)

    return redirect('/books/')


@login_required
def delete_book_order(request, book_order_id):
    BookOrder.objects.get(pk=book_order_id).delete()
    return redirect('/cart/')


@login_required
def checkout(request):
    form = OrderContactForm()

    context = {
        'form': form
    }
    return render(request, 'store/checkout.html', context)


@login_required
@transaction.atomic()
def add_order(request):
    cart_obj = Cart.objects.get(owner=request.user)

    order_contact = OrderContact.objects.create(
        street=request.POST['street'],
        number=request.POST['number'],
        city=request.POST['city'],
        bl=request.POST['bl'],
        sc=request.POST['sc'],
        ap=request.POST['ap'],
        county=request.POST['county'],
        phone=request.POST['phone'],
        email=request.POST['email']
    )

    Order.objects.create(
        owner=request.user,
        cart=cart_obj,
        contact=order_contact
    )

    # Decrement the quantity of remained books to purchase.
    for book_order in cart_obj.book_orders.all():
        book = book_order.book
        book.quantity = book.quantity - book_order.quantity
        book.save()

    # Remove owner from the cart. This will make the app create another cart in case of a new purchase.
    # The purchased carts will still exist.
    cart_obj.owner = None
    cart_obj.save()

    return redirect('/books/')


def check_owner(model, request):
    """Raise exception if the punishment does not belong to current user."""
    if model.owner != request.user:
        raise Http404


def details(request, book_id):
    context = {'book': Book.objects.get(id=book_id)}

    return render(request, 'store/details.html', context)


@login_required
def edit_book(request, book_id):
    """Edit book by given id. used by admin."""
    book_obj = Book.objects.get(id=book_id)

    if request.method != 'POST':
        # Initial request, fill form with current punishment data.
        form = BookForm(instance=book_obj)
    else:
        # Post data submitted.
        form = BookForm(instance=book_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:index')

    # It means the form was just opened and must be loaded, not saved.
    context = {'book': book_obj, 'form': form}
    return render(request, 'store/edit_book.html', context)
