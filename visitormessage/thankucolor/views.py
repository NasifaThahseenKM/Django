from django.shortcuts import render

def home(request):
    return render(request, 'thanku.html')

def result(request):
    username = request.GET.get('username')
    return render(request, 'thankuform.html', {
        'username': username,
        'formData': request.GET
    })
