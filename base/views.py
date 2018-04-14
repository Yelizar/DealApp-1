from django.shortcuts import render, redirect
from django.views.generic import View

from access.models import UserProfile
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

    def get(self, request):
        template = self.template_name
        try:
            self.current_user = Clients.objects.get(current_user=request.user)
            clients = self.current_user.members.all()
            return render(request, self.template_name, locals())
        except self.current_user.DoesNotExist:
            return render(request, self.template_name, locals())


def change_client(request, operator, pk):
    client = UserProfile.objects.get(pk=pk)
    if operator == 'add':
        Clients.make_client(request.user, client)
    elif operator == 'remove':
        Clients.remove_client(request.user, client)
    return redirect('base:clients')
