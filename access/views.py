from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from django.core.mail import send_mail
from DealApp import settings
from . import forms
from .models import UserProfile
from django.contrib.auth import authenticate, login
import os


class SignUpView(View):
    template = 'account/signup.html'

    def get(self, request, *args, **kwargs):
        template = self.template
        form = forms.SignUpForm()
        return render(request, template, locals())

    def post(self, request, *args, **kwargs):
        template = self.template
        form = forms.SignUpForm(request.POST)

        if form.is_valid():

            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.user_type = form.cleaned_data['user_type']
            if user.user_type == 'buyer':
                user.photo = 'access/profile_photo/default-ava.png'
            else:
                user.photo = 'access/profile_photo/avatar-s.png'
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

        return render(request, template, locals())




