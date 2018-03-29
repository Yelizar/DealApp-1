from django.shortcuts import render, get_object_or_404
from django.views.generic import View
# Create your views here.
from django.contrib.auth.models import User
from django.core.mail import send_mail
from DealApp import settings
from . import forms
from .models import UserProfile
from django.contrib.auth import authenticate, login


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
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

        return render(request, template, locals())




