from django.shortcuts import render, redirect

from clients.forms import OrderForm
from clients.models import Order


def order_create(request):
    order_form = OrderForm()

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_form.save()

            return redirect("clients:order-list")

    context = {"title": "Cadastrar Pedido", "order_form": order_form}

    return render(request, "clients/order_form.html", context)


def order_list(request):
    orders = Order.objects.all()

    context = {"orders": orders}

    return render(request, "clients/order_list.html", context)
