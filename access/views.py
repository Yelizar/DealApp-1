from django.shortcuts import render, get_object_or_404
from django.views.generic import View
# Create your views here.
from django.contrib.auth.models import User
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
        return render(request, template, locals())


class BuyerProfile(View):

    def get(self, request, username):
        user = User.objects.get(username=username)
        return render(request, 'access/User_profile/User_profile_page.html', locals())


