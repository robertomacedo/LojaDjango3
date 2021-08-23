from django import forms
from .models import Pedido_order, Cliente
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth.models import User


class Checar_PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_order
        fields = ["ordenado_pr", "endereco_envio", "telefone", "email"]
        widgets = {
            'ordenado_pr': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 200px;",
                'placeholder': "Ordenado por"
                }),

                'endereco_envio': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 200px;",
                'placeholder': "Endereço de envio"
                }),

                'telefone': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 200px;",
                'placeholder': "Telefone"
                }),

                'email': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 200px;",
                'placeholder': "Email"
                }),
        }



class RegistrarClienteForm(forms.ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Usuário', 'class': "form-control", 'style': 'max_width: 200px;display: flex;'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Senha', 'class': "form-control", 'style': 'max_width: 200px;display: flex;'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email', 'class': "form-control", 'style': 'max_width: 200px;display: flex;'}))
    class Meta:
        model = Cliente
        fields = ["usuario", "senha", "email", "nome_completo", "endereco"]
        widgets = {
            'usuario': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 200px;",
                'placeholder': "Usuário"
                }),

                'senha': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 200px;",
                'placeholder': "Senha"
                }),

                'email': EmailInput(attrs={
                'class': "form-control",
                'style': "max_width: 200px;",
                'placeholder': "Email"
                }),

                'nome_completo': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 200px;",
                'placeholder': "Nome completo"
                }),

                'endereco': TextInput(attrs={
                'class': "form-control",
                'style': "max_width: 200px;",
                'placeholder': "Endereço"
                }),
        }

    
    def limpar_username(self):
        uname = self.cleaned_data.get("usuario")
        if User.objects.filter(usuario=uname).exists():
            raise forms.ValidationError("Cliente já existe no bd")
        return uname