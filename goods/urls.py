from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'all_goods'

router = routers.DefaultRouter()
router.register('api/goods', views.GoodView, basename='goods')

urlpatterns = [
    path(r'all-goods/', views.AllGoodsView.as_view(), name='all_goods'),

    path(r'product/<int:product_id>', views.ProductDetailView.as_view(), name='product_view'),

    path('', include(router.urls))

]