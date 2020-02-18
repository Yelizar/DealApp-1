from django.forms import *
from tinymce.widgets import TinyMCE
from .models import Message


class MessageForm(ModelForm):
    message = CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ''}