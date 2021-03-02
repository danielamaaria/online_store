from django.contrib import admin

# Register your models here.
from store.models import Author, Category

admin.site.register(Category)
admin.site.register(Author)
