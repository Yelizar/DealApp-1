from rest_framework import serializers
from .models import UserProfile, Address


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'user_type')


class AddressSerializer(serializers.ModelSerializer):
    buyer = UserProfileSerializer(read_only=True)

    class Meta:
        model = Address
        fields = ('buyer', 'address')