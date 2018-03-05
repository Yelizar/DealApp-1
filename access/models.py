from django.db import models

# from django.contrib.auth.models import User
# Create your models here.


# class BuyerProfile(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     photo = models.ImageField('Profile photo', upload_to='access/profile_photo')
#     phone = models.CharField('Phone', default=None, blank=True, max_length=128)
#     map_location = models.CharField('location', default=None, blank=True, max_length=256)
#     is_active = models.BooleanField(default=True)
#
#     created = models.DateTimeField(auto_now=False, auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#
#     class Meta:
#         ordering = ['created']
#         verbose_name = 'User\'s profile'
#         verbose_name_plural = 'User\'s profiles'
#
#     def __str__(self):
#         return '{} {}'.format(self.user.first_name, self.user.last_name)






