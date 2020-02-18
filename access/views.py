from django.shortcuts import render, redirect
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout

from . import forms
from .models import UserProfile, user_photo_directory_path


class SignUpView(View):
    template_name = 'account/signup.html'

    def get(self, request, *args, **kwargs):
        template = self.template_name
        form = forms.SignUpForm()
        return render(request, template, locals())

    def post(self, request, *args, **kwargs):
        template = self.template_name
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user_type = form.cleaned_data['user_type']
            user_email = form.cleaned_data['email']

            user_obj = UserProfile.objects.get(username=username)

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
                    login(request, user_auth)
                    return redirect('buyers:buyer_home')
                elif user_type == 'supplier':
                    login(request, user_auth)
                    return redirect('suppliers:supplier_home')

        return render(request, template, locals())


class LogInView(View):
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        form = forms.LogInForm()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        form = forms.LogInForm(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            user_type = user.user_type
            if user_type == 'buyer':
                return redirect('buyers:buyer_home')
            elif user_type == 'supplier':
                return redirect('suppliers:supplier_home')
            else:
                return redirect('base:home')
        else:
            return render(request, self.template_name, locals())


def userlogout(request):
    logout(request)
    return redirect('base:home')
