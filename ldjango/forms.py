from django import forms
from .models import Pedido_order
from django.forms import ModelForm, TextInput, EmailInput, widgets


class Checar_PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_order
        fields = ["ordenado_pr", "endereco_envio", "telefone", "email"]
        widgets = {
            'ordenado_pr': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 300px;",
                'placehokder': "Ordenado por"
                }),

                'endereco_envio': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 300px;",
                'placehokder': "Endereço de envio"
                }),

                'telefone': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 300px;",
                'placehokder': "Telefone"
                }),

                'email': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 300px;",
                'placehokder': "Email"
                }),
        }



    