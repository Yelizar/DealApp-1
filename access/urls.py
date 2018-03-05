from django.urls import path, include
from . import views

app_name = 'access'
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="account_login"),
]