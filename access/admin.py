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
    list_display = ['id', 'username', 'user_type', 'is_active']
    fields = ['username', 'user_type', 'is_active','is_superuser', 'email', 'photo', 'phone', ]
    inlines = [BuyerAddressInLine]

    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)


class BuyerAddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields]


admin.site.register(Address, BuyerAddressAdmin)


class ClientsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Clients._meta.fields]


admin.site.register(Clients, ClientsAdmin)

