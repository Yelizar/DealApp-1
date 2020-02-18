from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [

    path('', views.EntireSearch, name='search'),
    path('all-users/', views.UsersView.as_view(), name='all-users')

]