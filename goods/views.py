from django.views.generic import View
from django.shortcuts import render

from .models import Goods, GoodsFeedback
from .forms import GoodsFeedbackForm

from itertools import chain
# Create your views here.


class AllGoodsView(View):
    template = 'goods/all_goods.html'

    def get(self, request):
        all_goods = Goods.objects.all()
        return render(request, self.template, locals())


class ProductDetailView(View):
    template_name = 'goods/product_detail.html'
    feedbacks = []

    def get(self, request, product_id):
        form = GoodsFeedbackForm()
        self.feedbacks = []
        try:
            product = Goods.objects.get(id=product_id)
            feedback = GoodsFeedback.objects.filter(product=product, comment=None)
            for feed in feedback:
                self.feedloop(feed)
            feedbacks = self.feedbacks
        except GoodsFeedback.DoesNotExist:
            feedback = None
        return render(request, self.template_name, locals())

    def feed_appender(self, feedback):
        for feed in feedback:
               self.feedloop(feed)

    #     return self.feedbacks
    def feedloop(self, feed):
        self.feedbacks.append(feed)
        feedback_replay = GoodsFeedback.objects.filter(comment=feed)
        if feedback_replay:
            self.feed_appender(feedback_replay)
