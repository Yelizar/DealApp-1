from django.shortcuts import render, get_object_or_404
from django.views.generic import View
# Create your views here.
from django.contrib.auth.models import User
from django.core.mail import send_mail
from DealApp import settings
from . import forms


class SignUpView(View):
    template = 'account/signup.html'

    def get(self, request, *args, **kwargs):
        template = self.template
        form = forms.FrameSignUpForm(initial={'username': 'Username'})
        return render(request, template, locals())

    def post(self, request, *args, **kwargs):
        template = self.template
        form = forms.FrameSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            """sending mail"""
            subject = 'Registration on DealApp'
            from_email = settings.EMAIL_HOST_USER
            to_email = ['Yelizar.Huryn@gmail.com']#we will take it from model
            signup_message = 'Hi you\'ve registered om DealApp '
            send_mail(subject=subject, from_email=from_email,\
                      recipient_list=to_email, message=signup_message, fail_silently=False)
        return render(request, template, locals())


class BuyerProfile(View):

    def get(self, request, username):
        user = User.objects.get(username=username)
        return render(request, 'access/User_profile/User_profile_page.html', locals())


