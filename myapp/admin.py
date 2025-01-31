from django.contrib import admin
from .models import User, Product

# Register your models here.


"""
  this section defines how the information will be displayed on the admin
  page. for example, list_display defines which rows will be displayed on the
  main admin info db page.
"""

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    list_filter = ('created_at', 'email')

"""
  this does the same but for products on the admin view.
"""

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('price', 'created_at')

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)