# thesis_searcher/thesis/web/urls.py

from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Assuming post_list is the view function in views.py
    # Add other URL patterns as needed
]
