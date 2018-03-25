from django.db import models
from access.models import *


class Session(models.Model):
    members = models.ManyToManyField(UserProfile)

    @models.permalink
    def get_absolute_url(self):
        return 'users:messages', (), {'session_id': self.pk}

class Message(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField('Enter your message')

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.message


