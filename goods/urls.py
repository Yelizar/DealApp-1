from django.urls import path
from . import views

app_name = 'all_goods'

urlpatterns = [
    path(r'all-goods/', views.AllGoodsView.as_view(), name='all_goods'),

    path(r'product/<int:product_id>', views.ProductDetailView.as_view(), name='product_view')
]