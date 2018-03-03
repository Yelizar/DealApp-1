from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    template_name = 'base/home.html'

    def get(self, request, **kwargs):
        return render (request, self.template_name)
