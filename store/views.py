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
    """Show all available books"""
    book_list: [] = Book.objects.order_by('date_added')
    context = {
        "books": book_list
    }
    return render(request, 'store/books.html', context)
