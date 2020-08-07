from django.shortcuts import render, redirect, get_object_or_404

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
    orders = Order.objects.select_related("client").all()

    context = {"orders": orders}

    return render(request, "clients/order_list.html", context)


def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_form = OrderForm(instance=order)

    if request.method == "POST":
        order_form = OrderForm(request.POST, instance=order)

        if order_form.is_valid():
            order_form.save()

            return redirect("clients:order-list")

    context = {"order_form": order_form}

    return render(request, "clients/order_form.html", context)


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    context = {"order": order}

    return render(request, "clients/order_detail.html", context)
