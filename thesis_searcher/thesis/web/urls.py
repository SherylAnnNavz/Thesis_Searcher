# thesis_searcher/thesis/web/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfirst, name='myfirst'),
    # Add other URL patterns as needed
]
