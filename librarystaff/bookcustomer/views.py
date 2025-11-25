from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from .models import Customer
from .forms import CustomerForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})


def view_books(request):
    books = Book.objects.all()
    return render(request, 'view_books.html', {'books': books})


def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_customers')
    else:
        form = CustomerForm()

    return render(request, 'add_customer.html', {'form': form})


def all_customers(request):
    customers = Customer.objects.all().order_by('name')
    return render(request, 'all_customers.html', {'customers': customers})


def filtered_customers(request):
    customers = Customer.objects.filter(email__endswith='@example.com')
    return render(request, 'filtered_customers.html', {'customers': customers})