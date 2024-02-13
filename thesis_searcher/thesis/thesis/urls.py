from django.contrib import admin
from django.urls import path
from web.views import thesis_list, thesis_detail  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', thesis_list, name="homepage"),  # Use thesis_list view for the homepage
    path('thesis/', thesis_list, name="thesis_list"),  # Add a URL pattern for the thesis list view
    path('thesis/<int:thesis_id>/', thesis_detail, name="post_detail"),  # Route for thesis detail view
]
