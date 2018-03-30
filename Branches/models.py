from django.db import models
from access.models import UserProfile
from django.utils import timezone


class Goods(models.Model):
    supplier = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=64, default=None, blank=True)
    price = models.FloatField('Price', default=0)
    picture = models.ImageField('Picture', upload_to='branches/goods', blank=True)
    description = models.TextField('Description', max_length=2048, default=None, blank=True)
    rating = models.IntegerField('Rating', default=0, null=True)

    is_active = models.BooleanField(default=True, blank=True)

    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name

