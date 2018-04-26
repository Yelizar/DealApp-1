from django import template
from chat.models import Session, Message
from django.db.models import Count

register = template.Library()


@register.simple_tag
def get_chats(user, companion):
    sessions = Session.objects.filter(members__in=[user, companion]).annotate(c=Count('members')).filter(c=2)
    chats = Message.objects.get(session=sessions[0])
    print(chats)
    return None
