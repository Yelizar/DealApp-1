from django.shortcuts import render
from django.views.generic import View, UpdateView, CreateView, DeleteView


from goods.models import Goods, UserProfile


class SupplierHomePage(View):
    template_name = 'supplier_pages/supplier_home.html'

    def get(self, request):
        return render(request, self.template_name, locals())


class SuppliersGoodsView(View):
    template_name = 'supplier_pages/list_goods.html'

    def get(self, request):
        template = self.template_name
        goods = Goods.objects.filter(supplier=request.user)
        # if request.is_ajax():
        #     try:
        #         if request.GET['data'] == 'get_page':
        #
        #             return render_to_response(template, locals())
        #     except KeyError:
        #         """"""
        return render(request, self.template_name, locals())


class SupplierGoodsCreateView(CreateView):
    template_name = 'supplier_pages/create_goods.html'
    model = Goods
    fields = ['name', 'price', 'picture', 'description']
    success_url = '../../goods/'

    def form_valid(self, form):
        supplier = UserProfile.objects.get(pk=self.request.user.id)
        form.instance.supplier = supplier
        return super(SupplierGoodsCreateView, self).form_valid(form)


class SupplierGoodsUpdateView(UpdateView):
    template_name = 'supplier_pages/update_goods.html'
    model = Goods
    success_url = '../../../goods/'
    fields = ['name', 'price', 'picture', 'description']

    def form_valid(self, form):
        supplier = UserProfile.objects.get(pk=self.request.user.id)
        form.instance.supplier = supplier
        return super(SupplierGoodsUpdateView, self).form_valid(form)


class SupplierGoodsDeleteView(DeleteView):
    template_name = 'supplier_pages/delete_goods.html'
    model = Goods
    success_url = '../../../goods/'
    fields = '__all__'
