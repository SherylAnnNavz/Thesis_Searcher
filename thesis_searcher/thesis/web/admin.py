from django.contrib import admin
from .models import Thesis

class ThesisAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('publication_date',)
    search_fields = ['title', 'abstract']

admin.site.register(Thesis, ThesisAdmin)
