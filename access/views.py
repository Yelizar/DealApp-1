from django.shortcuts import render, get_object_or_404, redirect, reverse
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
            user_id = UserProfile.objects.get(username=form.username)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user_type = form.cleaned_data['user_type']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user_type == 'buyer':

                    login(request, user)
                    return redirect('branches:list_goods', kwargs={'user_id': user_id})

        return render(request, template, locals())


class LogInView(View):
    template = 'account/login.html'

    def get(self, request, *args, **kwargs):
        template = self.template
        form = forms.LogInForm()
        return render(request, template, locals())

    def post(self, request, *args, **kwargs):
        template = self.template
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        user_obj = UserProfile.objects.get(username=user)
        user_type = user.user_type
        print(user_obj)
        print(user_type)
        if user is not None:
            if user_type == 'buyer':
                login(request, user)
                return redirect('buyers:buyer_home')
            elif user_type == 'supplier':
                login(request, user)
                return redirect('suppliers:supplier_home')
            else:
                return render(request, template, locals())

        return render(request, template, locals())


