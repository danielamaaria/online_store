from django.contrib import admin

# Register your models here.
from store.models import Author, Category, Book

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
