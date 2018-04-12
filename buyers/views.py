from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class BuyerHome(LoginRequiredMixin, View):
    template = 'buyer_pages/buyer_home.html'
    login_url = '/login/'
    redirect_field_name = 'required'

    def get(self, request):
        return render(request, self.template, locals())