from django.db import models


class Author(models.Model):
    """An entity that holds information about me, the author."""

    name = models.CharField(max_length=100, default=None)
    surname = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name + ' ' + self.surname


class Category(models.Model):
    """A model which describes the genre of a book. E.G. Drama, Comedy..."""

    category_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
