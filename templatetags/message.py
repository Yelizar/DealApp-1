from django import template
from chat.models import Message
from django.http import HttpResponse

register = template.Library()


@register.simple_tag
def message(request, id):
    messages = Message.objects.filter(session__members=id).exclude(user=id).filter(is_read=False)
    message = len(messages)
    if request.is_ajax():
        return HttpResponse(message, content_type='application/json')
    return message

