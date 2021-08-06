from django.urls import path 
from .views import *


app_name = "ldjango"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('todos-produtos/', TodosProdutosView.as_view(), name='todosprodutos'),
    path('produto/<slug:slug>/', ProdutoDetalhesView.as_view(), name='produtodetalhes'),
    path('addcarro-<int:pro_id>/', AddCarroView.as_view(), name='addcarro'),
    path('meu-carro/', MeuCarroView.as_view(), name='meu-carro'),
    path('manipular-carro/<int:cp_id>/', ManipularCarroView.as_view(), name='manipularcarro'),
]