from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def home2(request):
    return render(request, 'home2.html')

def about2(request):
    return render(request, 'about2.html')

def contact2(request):
    return render(request, 'contact2.html')