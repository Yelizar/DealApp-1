from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from access.models import UserProfile
from django.contrib.auth.decorators import login_required


class HomeView(View):
    template_name = 'base/home.html'

    def get(self, request):
        return render(request, self.template_name, locals())


class AboutUsView(View):
    template_name = 'base/about.html'

    def get(self, request):
        return render(request, self.template_name)

