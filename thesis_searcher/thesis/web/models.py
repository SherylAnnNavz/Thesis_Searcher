# models.py

from django.db import models
from django.contrib.auth.models import User


class Thesis(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='theses')
    publication_date = models.DateTimeField(auto_now=True)
    abstract = models.TextField()

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    thesis = models.ForeignKey(Thesis, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.created_at}"
