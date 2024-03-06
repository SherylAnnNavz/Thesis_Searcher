from django.shortcuts import render, get_object_or_404, redirect
from .models import Thesis, Comment
from .forms import CommentForm
from taggit.models import Tag

def thesis_list(request):
    theses = Thesis.objects.all()
    return render(request, 'post_list.html', {'theses': theses})

def thesis_detail(request, thesis_id):
    thesis = get_object_or_404(Thesis, id=thesis_id)
    comments = thesis.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thesis = thesis
            comment.save()
            return redirect('post_detail', thesis_id=thesis_id)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'thesis': thesis, 'comments': comments, 'form': form})

def thesis_search(request):
    query = request.GET.get('q')  
    if query:
        theses = Thesis.objects.filter(title__icontains=query) | Thesis.objects.filter(abstract__icontains=query)
    else:
        theses = Thesis.objects.all()

    return render(request, 'search_results.html', {'theses': theses, 'query': query})

def tagged_thesis(request, slug):
    tag = Tag.objects.get(slug=slug)
    theses = Thesis.objects.filter(tags__slug=slug)
    return render(request, 'tagged_theses.html', {'tag': tag, 'theses': theses})
