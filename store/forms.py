from django import forms
from .models import Book, OrderContact


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


class OrderContactForm(forms.ModelForm):
    class Meta:
        model = OrderContact
        fields = ['street', 'number', 'city', 'bl', 'sc', 'ap', 'county', 'phone', 'email']
        labels = {'street': 'Street',
                  'number': 'Nr.',
                  'city': 'City',
                  'bl': 'Bl.',
                  'sc': 'Sc.',
                  'ap': 'Ap.',
                  'county': 'County',
                  'phone': 'Contact Phone',
                  'email': 'Email (Optional)'}
