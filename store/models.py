from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list
from django.db import models


class Author(models.Model):
    """An entity that describes an author."""

    name = models.CharField(max_length=100, default=None)
    surname = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name + ' ' + self.surname


class Category(models.Model):
    """A model which describes the genre of a book. E.G. Drama, Comedy..."""

    name = models.CharField(max_length=200)
    is_child = models.BooleanField(default=True)  # It means this category is not parent
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    A model which describes the book entity. Each Book has a
    foreign key referencing the ID of a Category.
    """

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, editable=True)
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=150)
    url=models.URLField(default='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.publicdomainpictures.net%2Fpictures%2F60000%2Fnahled%2Fopen-book-1378562978Vki.jpg&f=1&nofb=1')

    class Meta:
        verbose_name_plural = 'books'

    def __str__(self):
        return self.title + ' By ' + str(self.author)


class Cart(models.Model):
    """A model which describes the book list before purchasing."""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.CharField(max_length=100, validators=[validate_comma_separated_integer_list])
