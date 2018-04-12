from django.shortcuts import render, HttpResponse
from django.views.generic import View
from access.models import UserProfile
from django.db.models import Q
# Create your views here.


def EntireSearch(request):
    template = 'search/search.html'

    query = request.GET.get('q')
    search_users = UserProfile.objects.filter(username__icontains=query)
    return render(request, template, locals())




