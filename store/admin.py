from django.contrib import admin

# Register your models here.
from store.models import Author, Category, Book, Cart

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Cart)
