from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    template_name = 'base/home.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)


class AboutUsView(View):
    template_name = 'base/about.html'


    def get(self, request, **kwargs):
        return render(request, self.template_name)

