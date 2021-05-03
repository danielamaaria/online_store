from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('buy_book/<int:book_id>/', views.buy_book, name='buy_book'),
    path('details/<int:book_id>/', views.details, name='details')
]