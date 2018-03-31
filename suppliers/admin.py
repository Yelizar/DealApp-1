from django.contrib import admin
from .models import *

class GoodsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Goods._meta.fields]

admin.site.register(Goods, GoodsAdmin)

