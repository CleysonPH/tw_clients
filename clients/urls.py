from django.urls import path

from .views import client_list, client_create, client_detail


app_name = "clients"
urlpatterns = [
    path("listar", client_list, name="client-list"),
    path("cadastrar", client_create, name="client-create"),
    path("<int:pk>/detalhes", client_detail, name="client-detail"),
]
