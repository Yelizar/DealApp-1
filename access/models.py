from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, User)
from django.contrib.auth.models import PermissionsMixin


class UserProfileManager(BaseUserManager):

    def create_user(self, username, password, email=None, user_type=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=username, email=self.normalize_email(email), user_type=user_type)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password,email, **kwargs):
        user = self.model(username=username, password=password, email=self.normalize_email(email))
        user.set_password(password)
        kwargs.setdefault('is_staff', True)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin, models.Model):
    TYPE = [('buyer', 'buyer'),
            ('supplier', 'supplier')]

    username = models.CharField(max_length=16, default=None, blank=True, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    photo = models.ImageField('Profile photo', upload_to='access/profile_photo', blank=True,
                              default='access/profile_photo/default-ava.png')
    phone = models.CharField('Phone', default=None, blank=True, max_length=128, null=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_superuser = models.BooleanField(default=False, blank=True)
    user_type = models.CharField(max_length=50, default=None, blank=True, choices=TYPE, null=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser


class Address(models.Model):
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.TextField(max_length=200, default=None, blank=False)

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Buyer\'s address'
        verbose_name_plural = 'Buyer\'s addresses'

    def __str__(self):
        return '{}'.format(self.buyer)






