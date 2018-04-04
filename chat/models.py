from django.db import models
from access.models import *
from django.utils import timezone


class Session(models.Model):
    members = models.ManyToManyField(UserProfile)

    @models.permalink
    def get_absolute_url(self):
        return 'chat:message', (), {'chat_id': self.pk}


class Message(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField('Enter your message')

    created = models.DateTimeField(default=timezone.now)
    is_readed = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.message


 