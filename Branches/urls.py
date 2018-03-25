from django.urls import path, re_path
from . import views

app_name = 'branches'

urlpatterns = [
    path(r'', views.UserHomePage.as_view(), name='User_home'),
]