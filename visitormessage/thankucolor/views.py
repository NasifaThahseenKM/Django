from django.shortcuts import render

def home(request):
    return render(request, 'thanku.html')

def result(request):
    username = request.GET.get('username')
    return render(request, 'thankuform.html', {
        'username': username,
        'formData': request.GET
    })


def color(request):
    # Display the input form
    return render(request, 'color.html')

def color_result(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        return render(request, 'colorform.html', {
            'name': name,
            'color': color,
            'formData': request.POST
        })
    else:
        # Redirect to form if someone visits result page directly
        return render(request, 'color.html')