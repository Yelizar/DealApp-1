from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):

    photo = models.ImageField('Profile photo', upload_to='access/profile_photo', blank=True)
    phone = models.CharField('Phone', null=True, default=None, blank=True, max_length=128)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    is_buyer = models.BooleanField(default=False, blank=False)
    is_supplier = models.BooleanField(default=False, blank=False)

    if is_buyer:
        map_location = models.CharField('location', null=True, default=None, blank=True, max_length=256)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Address(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.TextField(max_length=200, default=None, blank=False)

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Buyer\'s address'
        verbose_name_plural = 'Buyer\'s addresses'

    def __str__(self):
        return '{}'.format(self.owner)








