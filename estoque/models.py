from django.db import models

class Categoria(models.Model):
    titulo = models.CharField(max_length=40)
    
    def __str__(self):
        return self.titulo
    
class Produto(models.Model):
    descricao = models.CharField(max_length=40)
    ean = models.CharField(max_length=13)
    sku = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    quantidade = models.FloatField()
    preco_custo = models.FloatField()
    preco_venda = models.FloatField()

    def __str__(self) -> str:
        return self.descricao
    
    def gerar_desconto(self, desconto):
        return self.preco_venda - ((self.preco_venda * desconto) / 100)
    def lucro(self):
        lucro = self.preco_venda - self.preco_custo
        return (lucro * 100) / self.preco_custo
# Create your models here.
