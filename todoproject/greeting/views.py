from django.shortcuts import render

def greeting(request):
    # Just read values but do not show them
    email = request.GET.get('email')
    password = request.GET.get('password')

    # Always render the same page — empty form
    return render(request, 'index.html')
