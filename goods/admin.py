from django.contrib import admin

from .models import *


class GoodsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Goods._meta.fields]
    list_display_links = ['name']
    list_filter = ['name']

    search_fields = ['name', 'rating', 'supplier']


admin.site.register(Goods, GoodsAdmin)

