from django.shortcuts import render, render_to_response
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
        template = self.template_name
        if request.is_ajax():
            try:
                if request.GET['data'] == 'get_page':
                    return render_to_response(template, locals())
            except KeyError:
                return render(request, self.template_name)


