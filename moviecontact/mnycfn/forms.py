from django import forms
from .models import Movie
from .models import Contact

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'year']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone']