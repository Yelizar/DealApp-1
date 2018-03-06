from django.db import models
from django.contrib.auth.models import User


class BuyerProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField('Profile photo', upload_to='access/profile_photo')
    phone = models.CharField('Phone', default=None, blank=True, max_length=128)
    map_location = models.CharField('location', default=None, blank=True, max_length=256)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['created']
        verbose_name = 'Buyer\'s profile'
        verbose_name_plural = 'Buyer\'s profiles'

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class Address(models.Model):
    buyer = models.ForeignKey(BuyerProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, default=None, blank=False)
    address = models.TextField(max_length=200, default=None, blank=False)

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Buyer\'s address'
        verbose_name_plural = 'Buyer\'s addresses'

    def __str__(self):
        return '{}'.format(self.name)





