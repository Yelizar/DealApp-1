from django.urls import path, include
from rest_framework import routers

from . import views
from . import api

app_name = 'access'

router = routers.DefaultRouter()
router.register('users', api.UserProfileAPI, basename='user_profile')
router.register('address', api.AddressAPI, basename='address')

urlpatterns = [

    path("signup/", views.SignUpView.as_view(), name="signup"),

    path("login/", views.LogInView.as_view(), name="login"),

    path('logout/', views.userlogout, name='logout'),

    path('api/', include(router.urls))

]