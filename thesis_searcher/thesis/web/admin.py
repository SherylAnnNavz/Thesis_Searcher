from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','publication_date')
    list_filter = ("status",)
    search_fields = ['title', 'abstract']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)