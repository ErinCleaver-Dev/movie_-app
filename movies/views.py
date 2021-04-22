from django.shortcuts import render, redirect

# Create your views here.
from .models import Movie

def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_result = Movie.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {"search_result": search_result}
    return render(request, 'movies/movies_stuff.html', stuff_for_frontend)

def create(request):
    if request.method == 'POST':
        data = {
            'Name': request.POST.get('name'),
            'Picture': request.POST.get('picture'),
            'Rating': int(request.POST.get('rating')),
            'Notes': request.POST.get('notes'),
        }
        print(data)
        try:
            response = Movie.objects.create(
                name=data.get('Name'),
                picture=data.get('Picture'),
                rating=data.get('Rating'),
                notes=data.get('Notes')
            )
        except Exception as e:
            print(e)
            pass 

    return redirect('/')