from django.shortcuts import render
from django.views.generic import View


class ChatView(View):
    template_name = 'chat/chat.html'

    def get(self, request):
        template = self.template_name
        return render(request, template, locals())
