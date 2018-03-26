from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    TYPE = [('buyer', 'buyer'),
               ('supplier', 'supplier')]

    photo = models.ImageField('Profile photo', upload_to='access/profile_photo', blank=True, default='access/profile_photo/default_ava.png')
    phone = models.CharField('Phone', default=None, blank=True, max_length=128, null=True)

    user_type = models.CharField(max_length=50, default=None, blank=True, choices=TYPE, null=True)

    # def __str__(self):
    #     return '{}'.format(self.username)


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





