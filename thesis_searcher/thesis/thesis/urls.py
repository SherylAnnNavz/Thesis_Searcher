
from django.contrib import admin
from django.urls import path
from web.views import thesis_list, thesis_detail, thesis_search  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', thesis_list, name="homepage"),  
    path('thesis/', thesis_list, name="thesis_list"),  
    path('thesis/<int:thesis_id>/', thesis_detail, name="post_detail"), 
    path('search/', thesis_search, name="thesis_search"), 
]
