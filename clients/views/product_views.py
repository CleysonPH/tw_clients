from django.shortcuts import render, redirect

from clients.forms import ProductForm
from clients.models import Product


def product_create(request):
    product_form = ProductForm()

    if request.method == "POST":
        product_form = ProductForm(request.POST)

        if product_form.is_valid():
            product_form.save()

            return redirect("clients:product-list")

    context = {"title": "Cadastrar Produto", "product_form": product_form}

    return render(request, "clients/product_form.html", context)


def product_list(request):
    products = Product.objects.all()

    context = {"products": products}

    return render(request, "clients/product_list.html", context)
