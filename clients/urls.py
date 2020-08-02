from django.urls import path

from .views import client_list


app_name = "clients"
urlpatterns = [path("listar", client_list, name="clients-list")]
