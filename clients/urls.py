from django.urls import path

from .views import client_list, client_create


app_name = "clients"
urlpatterns = [
    path("listar", client_list, name="client-list"),
    path("cadastrar", client_create, name="client-create"),
]
