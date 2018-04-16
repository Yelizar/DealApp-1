from django.urls import path, include
from . import views

app_name = 'all_goods'

urlpatterns = [
    path(r'all-goods/', views.AllGoodsView.as_view(), name='all_goods'),

]