from clients.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
