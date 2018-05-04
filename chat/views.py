from django.shortcuts import render, redirect, reverse, render_to_response, HttpResponse
from django.views.generic import View
from django.db.models import Count
from django.core.mail import send_mail

from DealApp import settings
from .forms import *
from .models import Session, Message


class ChatView(View):
    template_name = 'chat/chat.html'

    def get(self, request):
        template = self.template_name
        chats = Session.objects.filter(members__in=[request.user.id])
        messages = Message.objects.filter(session__members=request.user.id).exclude(user=request.user.id).filter(is_read=False)
        message = len(messages)
        if request.is_ajax():
            try:
                if request.GET['data'] == 'get_page':
                    return render_to_response(template, locals())
            except KeyError:
                dat = message
                print(dat)
                return HttpResponse(dat)
        return render(request, self.template_name, locals())


class MessageView(View):
    template_name = 'chat/message.html'

    def get(self, request, chat_id):
        form = MessageForm()
        try:
            chat = Session.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_read=False).exclude(user=request.user).update(is_read=True)
            else:
                chat = None
        except Session.DoesNotExist:
            chat = None
        if request.is_ajax():
            try:
                if request.GET['data'] == 'get_message':
                    last_message = chat.message_set.last()
                    print(last_message)
                    return HttpResponse(last_message)
            except KeyError:

                return None
        return render(request, self.template_name, locals())

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.session_id = chat_id
            message.user = request.user
            message.save()


            content = form.cleaned_data['message']
            chat = Session.objects.filter(members__in=[request.user.id])
            # send_mail(subject=subject, from_email=settings.EMAIL_HOST_USER, recipient_list=[user_email],
            #           fail_silently=False, message=content)

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
