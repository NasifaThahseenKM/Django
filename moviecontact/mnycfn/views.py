from django.shortcuts import render
from .forms import MovieForm
from .forms import ContactForm

def movie_add(request):
    message = None

    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return render(request, 'movie_saved.html', {
                'movie': movie
            })
    else:
        form = MovieForm()

    return render(request, 'movie_form.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return render(request, 'thankyou.html', {
                'name': contact.full_name
            })
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})
