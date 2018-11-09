from django import forms

class cart_add_form(forms.Form):
    amount = forms.IntegerField()
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)