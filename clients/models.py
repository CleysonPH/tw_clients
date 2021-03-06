from django.db import models
from django.db.models.signals import m2m_changed


class Client(models.Model):
    GENDER_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções"),
    )

    name = models.CharField("Nome", max_length=100, null=False, blank=False)
    birth_date = models.DateField("Data de Nascimento", null=False, blank=False)
    email = models.EmailField("Email", null=False, blank=False)
    occupation = models.CharField("Profissão", max_length=50, null=False, blank=False)
    gender = models.CharField(
        "Sexo", max_length=1, choices=GENDER_CHOICES, blank=False, null=False
    )
    address = models.OneToOneField(
        "clients.Address",
        verbose_name="Endereço",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name


class Address(models.Model):
    street = models.CharField("Rua", max_length=200, null=False, blank=False)
    number = models.IntegerField("Número", null=False, blank=False)
    complement = models.CharField(
        "Complemento", max_length=200, null=False, blank=False
    )
    neighborhood = models.CharField("Bairro", max_length=50, null=False, blank=False)
    city = models.CharField("Cidade", max_length=50, null=False, blank=False)
    country = models.CharField("País", max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return self.street


class Order(models.Model):
    STATUS_CHOICE = (
        ("P", "Pedido Realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )

    client = models.ForeignKey(
        "clients.Client",
        verbose_name="Cliente",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    date = models.DateTimeField("Data", auto_now_add=True)
    value = models.FloatField("Valor", null=False, blank=False)
    status = models.CharField(
        "Status", max_length=1, choices=STATUS_CHOICE, null=False, blank=False
    )
    comments = models.TextField("Observações", blank=True, null=True)
    products = models.ManyToManyField("clients.Product", verbose_name="Produtos")

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return self.client.name


def pre_save_order_receiver(sender, instance, action, **kwargs):
    if action == "post_add" or action == "post_remove" or action == "post_clear":
        products = instance.products.all()
        order_total_price = 0

        for product in products:
            order_total_price += product.value
        instance.value = order_total_price
        instance.save()


m2m_changed.connect(pre_save_order_receiver, sender=Order.products.through)


class Product(models.Model):
    name = models.CharField("Nome", max_length=50, null=False, blank=False)
    description = models.TextField("Descrição")
    value = models.FloatField("Valor", null=False, blank=False)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name
