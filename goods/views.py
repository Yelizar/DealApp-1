from django.views.generic import View
from django.shortcuts import render, redirect, reverse

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
        feedbacks = []
        try:
            product = Goods.objects.get(id=product_id)
            feedback = GoodsFeedback.objects.filter(product=product, comment=None).order_by('pk')
            self.feed_appender(feedback)
            feedbacks += self.feedbacks
            print(feedbacks)
            self.feedbacks.clear()
        except GoodsFeedback.DoesNotExist:
            feedback = None
        return render(request, self.template_name, locals())

    def feed_appender(self, feedback):
        for feed in feedback:
            self.feedbacks.append(feed)
            self.feedloop(feed)

    def feedloop(self, feed):
        feedback_replay = GoodsFeedback.objects.filter(comment=feed).order_by('pk')
        if feedback_replay:
            self.feed_appender(feedback_replay)

    def post(self, request, product_id, **kwargs):
        form = GoodsFeedbackForm(data=request.POST)
        print(request.POST)

        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.product_id = product_id
            feedback.writer = request.user
            try:
                replay = GoodsFeedback.objects.get(id=request.POST['replay-comment-id'])
                feedback.comment = replay
            except ValueError:
                feedback.comment = None
            feedback.save()
        return redirect(reverse('all_goods:product_view', kwargs={'product_id': product_id}))

