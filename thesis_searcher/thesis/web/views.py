from django.shortcuts import render
from .models import Thesis

def thesis_list(request):
    theses = Thesis.objects.all()
    return render(request, 'post_list.html', {'web': theses})

def thesis_detail(request, thesis_id):
    thesis = Thesis.objects.get(id=thesis_id)
    return render(request, 'post_detail.html', {'web': thesis})
