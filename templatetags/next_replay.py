from django import template

register = template.Library()

@register.filter
def next(feedbacks, current_index):
    try:
        return feedbacks[int(current_index) + 1]
    except:
        return ''
