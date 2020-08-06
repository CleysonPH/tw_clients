from django.urls import path

from .views import (
    client_list,
    client_create,
    client_detail,
    client_update,
    client_delete,
    order_create,
    order_list,
    order_update,
)


app_name = "clients"
urlpatterns = [
    path("listar", client_list, name="client-list"),
    path("cadastrar", client_create, name="client-create"),
    path("<int:pk>/detalhes", client_detail, name="client-detail"),
    path("<int:pk>/editar", client_update, name="client-update"),
    path("<int:pk>/deletar", client_delete, name="client-delete"),
    path("pedido/cadastrar", order_create, name="order-create"),
    path("pedido/listar", order_list, name="order-list"),
    path("pedido/<int:pk>/editar", order_update, name="order-update"),
]
