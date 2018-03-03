from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField('Profile photo', upload_to='access/profile_photo')
    phone = models.CharField('Phone', default=None, blank=True, max_length=128)
    user_type = models.CharField('User type', default=None, blank=False, max_length=128)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


