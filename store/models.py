from django.db import models


class Author(models.Model):
    """An entity that holds information about me, the author."""

    name = models.CharField(max_length=100, default=None)
    surname = models.CharField(max_length=100, default=None)
