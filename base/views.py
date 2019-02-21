from django.shortcuts import render, redirect
from django.views.generic import View, DetailView

from access.models import UserProfile
from access.models import Clients
from goods.models import Goods


class HomeView(View):
    template_name = 'base/landing_home.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'base.html', locals())
        else:
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
        try:
            current_user = Clients.objects.get(current_user=request.user)
            clients = current_user.members.all()
            return render(request, self.template_name, locals())
        finally:
            return render(request, self.template_name, locals())


def change_client(request, operator, pk):
    client = UserProfile.objects.get(pk=pk)
    if operator == 'add':
        Clients.make_client(request.user, client)
    elif operator == 'remove':
        Clients.remove_client(request.user, client)
    return redirect('base:clients')


class SettingsDetailView(DetailView):
    template_name = 'base/settings.html'
    model = UserProfile

    def get_context_data(self, **kwargs):
        user = Clients.objects.get(current_user=kwargs['object'])
        clients = user.members.all()
        context = super().get_context_data(**kwargs)
        context['clients'] = clients
        if kwargs['object'] == 'buyer':
            return context
        elif kwargs['object'].user_type == 'supplier':
            goods = Goods.objects.filter(supplier=kwargs['object'])
            context['goods'] = goods
            return context
        else:
            return context
