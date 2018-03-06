from django.shortcuts import render, get_object_or_404
from django.views.generic import View
# Create your views here.
from allauth.account.views import LoginView
from django.contrib.auth.models import User


class LoginView(LoginView):

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())


class BuyerProfile(View):

    def get(self, request, username):
        user = User.objects.get(username=username)
        return render(request, 'access/User_profile/User_profile_page.html', locals())

