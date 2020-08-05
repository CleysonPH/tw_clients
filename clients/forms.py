from django import forms

from .models import Client, Address


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
