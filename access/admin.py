from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.


class BuyerAddressInLine(admin.TabularInline):
    model = Address
    extra = 0


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_buyer', 'is_supplier', 'date_joined')
    fields = ('photo', 'phone', 'map_location', 'is_buyer', 'is_supplier')
    inlines = [BuyerAddressInLine]


admin.site.register(UserProfile, UserProfileAdmin, )


class BuyerAddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields]


admin.site.register(Address, BuyerAddressAdmin)