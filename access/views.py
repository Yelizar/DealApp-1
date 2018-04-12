from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail
from . import forms
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
import os


class SignUpView(View):
    template = 'account/signup.html'

    def photo_choice(self, user_obj,  user_type):
        if user_type == 'buyer':
            user_obj.photo = 'access/profile_photo/default-ava.png'
            return user_obj.photo
        else:
            user_obj.photo = 'access/profile_photo/avatar-s.png'
            return user_obj.photo

    def get(self, request, *args, **kwargs):
        template = self.template
        form = forms.SignUpForm()
        return render(request, template, locals())

    def post(self, request, *args, **kwargs):
        template = self.template
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user_type = form.cleaned_data['user_type']
            user_email = form.cleaned_data['email']

            user_obj = UserProfile.objects.get(username=username)

            self.photo_choice(user_obj, user_type)

            user = form.save(commit=True)
            user_obj.save()

            email_subject = 'DealApp Email Confirmation'
            email_content = 'Welcome ' + username + ', ' + \
                            'now your are registered on http://127.0.0.1:8000/'

            user_auth = authenticate(request, username=username, password=password)
            if user_auth is not None:
                send_mail(subject=email_subject, from_email=settings.EMAIL_HOST_USER, recipient_list=[user_email],
                          message=email_content,
                          fail_silently=False)

                if user_type == 'buyer':
                    print(user_type)
                    login(request, user_auth)
                    return redirect('buyers:buyer_home')
                elif user_type == 'supplier':
                    print(user_type)
                    login(request, user_auth)
                    return redirect('suppliers:supplier_home')

        return render(request, template, locals())


class LogInView(View):
    template = 'account/login.html'

    def get(self, request, *args, **kwargs):
        template = self.template
        form = forms.LogInForm()
        return render(request, template, locals())

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        user_type = user.user_type
        login(request, user)
        if user is not None:
            if user_type == 'buyer':
                return redirect('buyers:buyer_home')
            elif user_type == 'supplier':
                return redirect('suppliers:supplier_home')
        return redirect('base:home')


def userlogout(request):
    logout(request)
    return redirect('base:home')

