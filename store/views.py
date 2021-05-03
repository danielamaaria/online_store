from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from store.forms import BookForm
from store.models import Book


def index(request):
    context = {
        'header': ''
    }
    return render(request, 'store/index.html', context)


@login_required
def books(request):
    """Show all available books."""
    book_list: [] = Book.objects.order_by('date_added')
    context = {
        "books": book_list
    }
    return render(request, 'store/books.html', context)


@login_required
def buy_book(request, book_id):
    return redirect('/store/index.html')


@login_required
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
