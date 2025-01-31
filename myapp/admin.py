from django.contrib import admin
from django.contrib.auth.models import User  # Import Django's User
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'date_created')
    list_filter = ('date_created', 'author')

admin.site.register(Blog, BlogAdmin)
# No need to register User again as it's already registered by Django