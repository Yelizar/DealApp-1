from django.urls import path

from . import views

app_name = 'buyers'

urlpatterns = [

    path(r'home-b/', views.BuyerHome.as_view(), name='buyer_home')

]