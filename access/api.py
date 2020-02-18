from rest_framework import viewsets
from .models import UserProfile, Address
from .serializers import UserProfileSerializer, AddressSerializer


class UserProfileAPI(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class AddressAPI(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer