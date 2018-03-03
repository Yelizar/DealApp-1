from django.contrib import admin
from .models import *
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

admin.site.register(Product, ProductsAdmin)