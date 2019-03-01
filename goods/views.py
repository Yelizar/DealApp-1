from django.views.generic import View
from django.shortcuts import render

from .models import Goods
# Create your views here.


class AllGoodsView(View):
    template = 'goods/all_goods.html'

    def get(self, request):
        all_goods = Goods.objects.all()
        return render(request, self.template, locals())
