from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
def details(request, id):
    """Show all available details of a book."""
    book = Book.objects.filter(pk=id)
    if not book:
        raise FileNotFoundError

    context = {"book": book[0]}
    return render(request, 'store/details.html', context)
