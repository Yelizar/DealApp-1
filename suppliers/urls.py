from django.urls import path

from . import views

app_name = 'suppliers'

urlpatterns = [

    path(r'home-s/', views.SupplierHomePage.as_view(), name='supplier_home'),

    path(r'goods/', views.SuppliersGoodsView.as_view(), name='list_goods'),

    path(r'goods/create/', views.SupplierGoodsCreateView.as_view(), name='crete_goods'),

    path(r'goods/update/<int:pk>/', views.SupplierGoodsUpdateView.as_view(), name='update_goods'),

    path(r'goods/delete/<int:pk>/', views.SupplierGoodsDeleteView.as_view(), name='delete_goods'),

]