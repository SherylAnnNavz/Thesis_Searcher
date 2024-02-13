from django.contrib import admin
from django.urls import path
from web.views import thesis_list, thesis_detail  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', thesis_list, name="homepage"),  # Use thesis_list view for the homepage
    path('thesis/<int:thesis_id>/', thesis_detail, name="thesis_detail"),  # Route for thesis detail view
]
