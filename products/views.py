from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic import DetailView

from .models import Product, About


class ProductListView(generic.ListView):
    template_name = 'products/products.html'
    context_object_name = 'products_list'
    model = Product

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class ProductDetailView(generic.DetailView):
    template_name = 'products/products_detail.html'
    context_object_name = 'product'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(Product, id=product_id)


class LaptopsListView(generic.ListView):
    template_name = "products/laptops.html"
    context_object_name = "laptops"
    model = Product

    def get_queryset(self):
        return Product.objects.filter(category__name="Ноутбуки").order_by("-id")


class LaptopsDetailView(DetailView):
    model = Product
    template_name = "products/laptop_detail.html"
    context_object_name = "laptops_detail"

    def get_object(self):
        laptop_id = self.kwargs.get("id")
        return get_object_or_404(Product, id=laptop_id)


def store_description(request):
    description = get_object_or_404(About)
    return render(request, 'store_description.html', {'description': description})


class ComputerListView(generic.ListView):
    template_name = "products/computers.html"
    context_object_name = "pc"
    model = Product

    def get_queryset(self):
        return Product.objects.filter(category__name="Компьютеры").order_by("-id")


class ComputerDetailView(DetailView):
    model = Product
    template_name = "products/pc_detail.html"
    context_object_name = "pc_detail"

    def get_object(self):
        computer_id = self.kwargs.get("id")
        return get_object_or_404(Product, id=computer_id)
