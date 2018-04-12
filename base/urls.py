from django.urls import path

from . import views

app_name = 'base'

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),

    path('about/', views.AboutUsView.as_view(), name='about'),

    path('clients/', views.ClietnsView.as_view(), name='clients'),

    path('clients/<slug:operator>/<int:pk>', views.change_client, name='change_clients')

]