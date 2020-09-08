from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'state', 'creation_date',)

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['names', 'last_names', 'email']
    list_display = ('names', 'last_names', 'email', 'state', 'creation_date',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
