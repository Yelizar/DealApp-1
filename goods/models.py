from django.db import models
from django.utils import timezone

from access.models import UserProfile


def user_goods_directory_path(instance, filename):
    return 'suppliers/{0}/goods/{1}'.format(instance.supplier.username, filename)


class Goods(models.Model):
    supplier = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, default=None, blank=True)
    price = models.FloatField('Price', default=0)
    picture = models.ImageField('Picture', upload_to=user_goods_directory_path, blank=True)
    description = models.TextField('Description', max_length=2048, default=None, blank=True)
    rating = models.IntegerField('Rating', default=0, null=True)

    is_active = models.BooleanField(default=True, blank=True)

    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created']
        verbose_name = 'Goods'
        verbose_name_plural = 'Goods'

    def __str__(self):
        return self.name
