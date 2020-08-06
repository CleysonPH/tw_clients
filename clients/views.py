from django.shortcuts import render, redirect, get_object_or_404

from .models import Client
from .forms import ClientForm, AddressForm


def client_list(request):
    clients = Client.objects.all()

    context = {"clients": clients}

    return render(request, "clients/client_list.html", context)


def client_create(request):
    client_form = ClientForm()
    address_form = AddressForm()
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        address_form = AddressForm(request.POST)

        if client_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            client = client_form.save(commit=False)
            client.address = address
            client.save()

            return redirect("clients:client-list")
    context = {"client_form": client_form, "address_form": address_form}
    return render(request, "clients/client_form.html", context)


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)

    context = {"client": client}

    return render(request, "clients/client_detail.html", context)


def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)

    client_form = ClientForm(instance=client)
    address_form = AddressForm(instance=client.address)

    if request.method == "POST":
        client_form = ClientForm(request.POST, instance=client)
        address_form = AddressForm(request.POST, instance=client.address)

        if client_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            client = client_form.save(commit=False)
            client.address = address
            client.save()

            return redirect("clients:client-detail", pk=client.pk)
    context = {"client_form": client_form, "address_form": address_form}
    return render(request, "clients/client_form.html", context)


def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == "POST":
        client.address.delete()
        client.delete()

        return redirect("clients:client-list")
    context = {"client": client}
    return render(request, "clients/client_confirm_delete.html", context)
