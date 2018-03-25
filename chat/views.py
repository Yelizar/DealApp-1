from django.shortcuts import render
from django.views.generic import View
from .models import Session


class ChatView(View):
    template_name = 'chat/chat.html'

    def get(self, request):
        template = self.template_name
        chat = Session.objects.filter(members__in=[request.user.id])
        return render(request, template, locals())


