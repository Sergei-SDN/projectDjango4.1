from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.forms import inlineformset_factory
from Product.models import Product, Version
from catalog.forms import ProductForm, VersionForm
from catalog.services import get_cached_category_for_product


# Create your views here.

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SkyStore'
        products = Product.objects.all()
        active_versions = {}
        for product in products:
            active_versions[product] = Version.objects.filter(product=product, is_current=True).first()
            context['active_versions'] = active_versions
        return context


# def home(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list,
#         'title': 'SkyStore'
#     }
#     return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SkyStore'
        return context


# def product_detail(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#         'title': f'SkyStore {product_item.name}'
#     }
#     return render(request, 'catalog/product_detail.html', context)

class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SkyStore'
        products = Product.objects.all()
        active_versions = {}
        for product in products:
            active_versions[product] = Version.objects.filter(product=product, is_current=True).first()
            context['active_versions'] = active_versions
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class VersionCreateView(CreateView):
    model = Version
    template_name = 'catalog/version_form.html'
    form_class = VersionForm
    success_url = reverse_lazy('catalog:home')


class VersionUpdateView(UpdateView):
    model = Version
    template_name = 'catalog/version_form.html'
    form_class = VersionForm
    success_url = reverse_lazy('catalog:home')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     ParentFormset = inlineformset_factory()
    #
    #     return context
    #
    # def form_valid(self, form):
    #     return super().form_valid(form)
