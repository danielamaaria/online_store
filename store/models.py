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
    is_child = models.BooleanField(default=True)  # It means this category has books referencing it.
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        if self.is_child:
            return self.name + ' (child)'
        return self.name + ' (parent)'


class Book(models.Model):
    """
    A model which describes the book entity. Each Book has a
    foreign key referencing the ID of a Category.
    """

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)

    class Meta:
        verbose_name_plural = 'books'

    def __str__(self):
        return self.title + ' By ' + str(self.author)
