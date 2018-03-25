from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from access.models import UserProfile


class HomeView(View):
    template_name = 'base/home.html'
    # user = UserProfile.objects.all()

    def get(self, request):
        return render(request, self.template_name, locals())


class AboutUsView(View):
    template_name = 'base/about.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)

