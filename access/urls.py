from django.urls import path, re_path
from . import views

app_name = 'access'
urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="account_login"),
    re_path(r'^(?P<username>\w+)/$', views.BuyerProfile.as_view(), name='buyer_profile'),
]