from django.shortcuts import render, render_to_response
from django.views.generic import View
from django.contrib.auth.models import User
from access.models import UserProfile
from django.contrib.auth.decorators import login_required
from access.models import Clients


class HomeView(View):
    template_name = 'base/home.html'

    def get(self, request):
        return render(request, self.template_name, locals())


class AboutUsView(View):
    template_name = 'base/about.html'

    def get(self, request):
        template = self.template_name
        # if request.is_ajax():
        #     try:
        #         if request.GET['data'] == 'get_page':
        #             return render_to_response(template, locals())
        #     except KeyError:
        #         return render(request, self.template_name)
        return render(request, self.template_name, locals())


class ClietnsView(View):
    template_name ='base/clients.html'

    def get(self, request, id):
        template = self.template_name
        user = UserProfile.objects.filter(id=id)
        clients = Clients.objects.filter(members__in=[id])
        print(clients)
        return render(request, self.template_name, locals())
