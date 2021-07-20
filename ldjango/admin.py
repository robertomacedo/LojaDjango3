from django.contrib import admin
from .models import *


admin.site.register([Cliente, Produto, Categoria, Carro, CarroProduto, Pedido_order])
