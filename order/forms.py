from django import forms
from .models import Order

class order_create_form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'email', 'address', 'postal_code', 'city']