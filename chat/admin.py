from django.contrib import admin

from .models import *


class SessionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Session._meta.fields]


admin.site.register(Session, SessionAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Session._meta.fields]


admin.site.register(Message, MessageAdmin)
