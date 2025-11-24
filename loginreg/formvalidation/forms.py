from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Login Form (Gmail not allowed)
def validate_not_gmail(value):
    if "@gmail" in value.lower():
        raise ValidationError("Gmail addresses are not allowed.")

class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=100,
        validators=[validate_email, validate_not_gmail],
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

# Registration Form (built-in validation only)
class RegistrationForm(forms.Form):
    full_name = forms.CharField(
        min_length=5,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'})
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )
