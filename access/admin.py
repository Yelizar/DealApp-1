from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.


class BuyerAddressInLine(admin.TabularInline):
    model = Address
    extra = 0


class BuyerProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BuyerProfile._meta.fields]
    inlines = [BuyerAddressInLine]


admin.site.register(BuyerProfile, BuyerProfileAdmin, )


class BuyerAddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields]


admin.site.register(Address, BuyerAddressAdmin)