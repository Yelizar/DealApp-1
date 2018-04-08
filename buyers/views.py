from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class BuyerHome(View):
    template = 'buyer_pages/buyer_home.html'

    def get(self, request):
        print(1)
        return render(request, self.template, locals())