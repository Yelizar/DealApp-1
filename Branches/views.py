from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth.models import User
from access.models import UserProfile
# Create your views here.


class UserHomePage(View):
    b_template = 'buyer_pages/buyer_home.html'
    s_template = 'supplier_pages/supplier_home.html'
    landing_template = 'base/home.html'

    def get(self, request):

        if request.user.is_authenticated:
            if request.user.user_type == 'buyer':
                return render(request, self.b_template)
            else:
                return render(request, self.s_template)
        else:
            return redirect('/')