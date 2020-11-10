from django import forms
from .models import Order
from django.contrib.auth.models import User


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email',  'postal_code', 'city', 'street',]
        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя"}),
            'last_name': forms.TextInput(attrs={"class": "form-control", "placeholder": "Фамилия"}),
            'email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "e-mail"}),
            'postal_code': forms.TextInput(attrs={"class": "form-control", "placeholder": "Почтовый индекс"}),
            'city': forms.TextInput(attrs={"class": "form-control", "placeholder": "Город"}),
            'street': forms.TextInput(attrs={"class": "form-control", "placeholder": "Улица"}),

            }

  
