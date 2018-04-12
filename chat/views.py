from django.shortcuts import render, redirect, reverse, render_to_response
from django.views.generic import View
from django.db.models import Count
from .forms import *
from .models import Session
from django.http import HttpResponse


class ChatView(View):
    template_name = 'chat/chat.html'

    def get(self, request):
        template = self.template_name
        chats = Session.objects.filter(members__in=[request.user.id])
        messages = Message.objects.filter(session__members=request.user.id).exclude(user=request.user.id).filter(is_readed=False)
        message = len(messages)
        if request.is_ajax():
            try:
                if request.GET['data'] == 'get_page':
                    return render_to_response(template, locals())
            except KeyError:
                dat = message
                return render(request, self.template_name, locals())


class MessageView(View):
    template_name = 'chat/message.html'

    def get(self, request, chat_id):
        form = MessageForm()
        try:
            chat = Session.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(user=request.user).update(is_readed=True)
            else:
                chat = None
        except Session.DoesNotExist:
            chat = None

        return render(request, self.template_name, locals())

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.session_id = chat_id
            message.user = request.user
            message.save()
        return redirect(reverse('chat:message', kwargs={'chat_id': chat_id}))


class CreateSessionView(View):
    def get(self, request, user_id):
        chats = Session.objects.filter(members__in=[request.user.id, user_id]).annotate(c=Count('members')).filter(c=2)

        if chats.count() == 0:
            chat = Session.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('chat:message', kwargs={'chat_id': chat.id}))
