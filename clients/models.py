from django.db import models


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
        verbose_name="Pedido",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    date = models.DateTimeField("Data", auto_now_add=True)
    value = models.FloatField("Valor", null=False, blank=False)
    status = models.CharField(
        "Status", max_length=1, choices=STATUS_CHOICE, null=False, blank=False
    )
    comments = models.TextField("Observações")

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return self.client.name
