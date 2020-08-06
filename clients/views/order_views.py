from django.shortcuts import render

from clients.forms import OrderForm


def order_create(request):
    order_form = OrderForm()

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_form.save()

    context = {"title": "Cadastrar Pedido", "order_form": order_form}

    return render(request, "clients/order_form.html", context)
