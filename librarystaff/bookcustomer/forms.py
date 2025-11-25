from django import forms
from .models import Book
from .models import Customer

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']