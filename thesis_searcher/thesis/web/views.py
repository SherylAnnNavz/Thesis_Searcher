# views.py

from django.shortcuts import render
from .models import Thesis

def thesis_list(request):
    theses = Thesis.objects.all()
    return render(request, 'post_list.html', {'theses': theses})

def thesis_detail(request, thesis_id):
    thesis = Thesis.objects.get(id=thesis_id)
    return render(request, 'post_detail.html', {'thesis': thesis})

def thesis_search(request):
    query = request.GET.get('q')  # Get the search query from the URL parameters
    if query:
        theses = Thesis.objects.filter(title__icontains=query) | Thesis.objects.filter(abstract__icontains=query)
    else:
        theses = Thesis.objects.all()  # If no query is provided, return all theses

    return render(request, 'search_results.html', {'theses': theses, 'query': query})
