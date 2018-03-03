from django.db import models

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=128, default=None, blank=False)
    price = models.FloatField(default=0, blank=False)

    def __str__(self):
        return '{}'.format(self.name)

