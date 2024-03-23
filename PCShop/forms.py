from django import forms

class OrderForm(forms.Form):
    email = forms.EmailField(max_length=50, required=True)
    phone = forms.CharField(max_length=20, required=True)
    