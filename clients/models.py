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

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name
