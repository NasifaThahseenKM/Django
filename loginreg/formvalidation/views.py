from django.shortcuts import render
from .forms import LoginForm, RegistrationForm  # make sure to import RegistrationForm

# Existing login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            return render(request, 'thankyou.html', {'email': email})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            return render(request, 'thankyou2.html', {'full_name': full_name})
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
