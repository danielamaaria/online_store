from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        instance = getattr(self, 'instance', None)

        if instance and instance.id:
            self.fields['title'].widget.attrs['readonly'] = True
            self.fields['author'].widget.attrs['readonly'] = True
            self.fields['price'].widget.attrs['readonly'] = True
            self.fields['category'].widget.attrs['readonly'] = True

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'category']
        labels = {'title': 'Title',
                  'author': 'Author',
                  'price': 'Price',
                  'category': 'Category'}
