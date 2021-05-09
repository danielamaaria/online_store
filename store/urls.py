from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('cart/', views.cart, name='cart'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('buy_book/<int:book_id>/', views.buy_book, name='buy_book'),
    path('details/<int:book_id>/', views.details, name='details'),
    path('delete_book_order/<int:book_order_id>/', views.delete_book_order, name='delete_book_order'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_order/', views.add_order, name='add_order'),
]