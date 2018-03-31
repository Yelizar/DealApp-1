from django.urls import path, re_path
from . import views

app_name = 'suppliers'

urlpatterns = [
    path(r'', views.SupplierHomePage.as_view(), name='supplier_home'),
    path(r'goods/', views.SuppliersGoodsView.as_view(), name='list_goods'),
    path(r'goods/create/', views.SupplierGoodsCreateView.as_view(), name='crete_goods'),

]