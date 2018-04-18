from django.shortcuts import render, HttpResponse
from django.views.generic import View
from goods.models import Goods

from access.models import UserProfile
# Create your views here.


def EntireSearch(request):
    template = 'search/search.html'

    query = request.GET.get('q')
    search_users = UserProfile.objects.filter(username__icontains=query)[0:4]
    search_products = Goods.objects.filter(name__icontains=query)[0:4]

    return render(request, template, locals())
