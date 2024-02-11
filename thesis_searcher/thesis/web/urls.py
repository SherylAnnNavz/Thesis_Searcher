from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='myfirst'),  # Change 'myfirst' to match the name in your URL pattern
    # Add other URL patterns as needed
]
