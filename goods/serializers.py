from rest_framework import serializers
from .models import Goods
from access.serializers import UserProfileSerializer
from access.models import UserProfile
from django.contrib.auth import get_user_model


class GoodsSerializers(serializers.ModelSerializer):
    supplier = UserProfileSerializer(read_only=True)

    class Meta:
        model = Goods
        fields = ('id', 'price', 'supplier')
