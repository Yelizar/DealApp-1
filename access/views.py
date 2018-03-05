from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from allauth.account.views import LoginView

class LoginView(LoginView):

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

