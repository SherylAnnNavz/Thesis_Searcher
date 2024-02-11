# Correcting the import statement in urls.py
from django.urls import path
from . import views  # Assuming views.py is in the same directory as urls.py

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Assuming you want to display the post list view on the homepage
    # Add other URL patterns as needed
]
