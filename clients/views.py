from django.shortcuts import render, redirect, get_object_or_404

from .models import Client
from .forms import ClientForm


def client_list(request):
    clients = Client.objects.all()

    context = {"clients": clients}

    return render(request, "clients/client_list.html", context)


def client_create(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("clients:client-list")
    context = {"form": form}
    return render(request, "clients/client_form.html", context)


def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)

    context = {"client": client}

    return render(request, "clients/client_detail.html", context)


def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(instance=client)

    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()

            return redirect("clients:client-detail", pk=client.pk)
    context = {"form": form}
    return render(request, "clients/client_form.html", context)


def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == "POST":
        client.delete()

        return redirect("clients:client-list")
    context = {"client": client}
    return render(request, "clients/client_confirm_delete.html", context)
