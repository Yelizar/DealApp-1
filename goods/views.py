from django.views.generic import View
from django.shortcuts import render

from .models import Goods, GoodsFeedback
from .forms import GoodsFeedbackForm
# Create your views here.


class AllGoodsView(View):
    template = 'goods/all_goods.html'

    def get(self, request):
        all_goods = Goods.objects.all()
        return render(request, self.template, locals())


class ProductDetailView(View):
    template_name = 'goods/product_detail.html'

    def get(self, request, product_id):
        form = GoodsFeedbackForm()
        try:
            product = Goods.objects.get(id=product_id)
            feedback = GoodsFeedback.objects.filter(product=product)
        except GoodsFeedback.DoesNotExist:
            feedback = None
        return render(request, self.template_name, locals())
