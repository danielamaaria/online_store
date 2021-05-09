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
    quantity = models.IntegerField(default=5)
    date_added = models.DateTimeField(auto_now_add=True)
    first_published = models.IntegerField(default=1900)
    description = models.TextField(max_length=500)
    url = models.URLField(
        default='https://digitalsynopsis.com/wp-content/uploads/2016/06/negative-space-design-art-illustration-ads-30.jpg')

    class Meta:
        verbose_name_plural = 'books'

    def __str__(self):
        return self.title + ' By ' + str(self.author)


class BookOrder(models.Model):
    """A model which holds the relation between the quantity and the purchased book."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    # Calculate price of all books together.
    def price(self):
        return self.book.price * self.quantity


class Cart(models.Model):
    """A model which describes the book list before purchasing."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book_orders = models.ManyToManyField(BookOrder, editable=True)

    def total(self):
        total = 0.0
        for book_order in self.book_orders.all():
            total = total + book_order.price()
        return total


class OrderContact(models.Model):
    """A model which describes an address and other contact info."""

    class Meta:
        verbose_name_plural = 'contacts'

    street = models.CharField(max_length=200)
    number = models.IntegerField()
    city = models.CharField(max_length=200)
    bl = models.CharField(max_length=50, null=True)
    sc = models.CharField(max_length=50, null=True)
    ap = models.CharField(max_length=50, null=True)
    county = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)


class Order(models.Model):
    """A model which describes a previous purchase."""

    class Meta:
        verbose_name_plural = 'orders'

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    contact = models.ForeignKey(OrderContact, on_delete=models.DO_NOTHING)
