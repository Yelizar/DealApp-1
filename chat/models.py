from django.utils import timezone
from tinymce.models import HTMLField


from access.models import *


class Session(models.Model):
    members = models.ManyToManyField(UserProfile)

    def get_absolute_url(self):
        return 'chat:message', (), {'chat_id': self.pk}


class Message(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = HTMLField()

    created = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.message
