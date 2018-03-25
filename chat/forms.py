from django.forms import *
from .models import Message


class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ''}