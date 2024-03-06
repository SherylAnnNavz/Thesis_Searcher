from django.contrib import admin
from django.urls import path
from web.views import thesis_list, thesis_detail, thesis_search, tagged_thesis  # Correct the import statement to use the correct view function name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', thesis_list, name="homepage"),  
    path('thesis/', thesis_list, name="thesis_list"),  
    path('thesis/<int:thesis_id>/', thesis_detail, name="post_detail"), 
    path('search/', thesis_search, name="thesis_search"), 
    path('tag/<slug:slug>/', tagged_thesis, name='tagged_thesis'),  # Update the view function name here
]