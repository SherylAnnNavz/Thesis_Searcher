# views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status=1).order_by('-publication_date')
    return render(request, 'post_list.html', {'posts': posts})
