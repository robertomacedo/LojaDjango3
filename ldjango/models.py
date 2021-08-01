from django.db import models
from django.contrib.auth.models import User
# from django.db.models.fields import PositiveIntegerField


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    data_cad = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo


class Categoria(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo


class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="produtos")
    preco_mercado = models.PositiveIntegerField()
    vend = models.PositiveIntegerField()
    descricao = models.TextField()
    garantia = models.CharField(max_length=300, null=True, blank=True)
    devolucao = models.CharField(max_length=300, null=True, blank=True)
    visualizacao = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.titulo


class Carro(models.Model):
    cliente = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    data_em = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return "Carro" + str(self.id)


class CarroProduto(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    avaliacao = models.PositiveIntegerField()
    quantidade = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self) -> str:
        return "Carro" + str(self.carro.id) + "CarroProduto:" + str(self.id)

PEDIDO_STATUS = (
    ('pedito recebido', 'Pedido Recebido'),
    ('pedido processando', 'Pedido Processando'),
    ('pedido a caminho', 'Pedido a caminho'),
    ('pedido completado', 'Pedido completado'),
    ('pedido cancelado', 'Pedido cancelado'),
)


class Pedido_order(models.Model):
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE)
    ordenado_pr = models.CharField(max_length=200)
    endereco_envio = models.CharField(max_length=200)
    telefone = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    endereco_envio = models.CharField(max_length=200)
    subtotal = models.PositiveIntegerField()
    desconto = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    pedido_status = models.CharField(max_length=50, choices=PEDIDO_STATUS)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "Pedido_order:" + str(self.id)