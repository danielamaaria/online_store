from django.contrib import admin

# Register your models here.
from store.models import Author, Category, Book, Cart, BookOrder, Order, OrderContact

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(BookOrder)
admin.site.register(Order)
admin.site.register(OrderContact)
