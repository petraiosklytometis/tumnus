from django.db import models

class Categoria(models.Model):
    titulo = models.CharField(max_length=40)
    
    def __str__(self):
        return self.titulo
    

class Produto(models.Model):
    descricao = models.CharField(max_length=40)
    # TODO: Buscar Produto no Cosmos pelo EAN
    ean = models.CharField(max_length=13)
    sku = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    quantidade = models.FloatField()
    preco_custo = models.FloatField()
    # TODO: Fazer cálculo de preço por BinaryField
    preco_venda = models.FloatField()

    def __str__(self) -> str:
        return self.descricao
    
    def gerar_desconto(self, desconto):
        # TODO: Gerar desconto por quantidade no PDV
        return self.preco_venda - ((self.preco_venda * desconto) / 100)
    def lucro(self):
        lucro = self.preco_venda - self.preco_custo
        return (lucro * 100) / self.preco_custo
    
class Imagem(models.Model):
    imagem = models.ImageField(upload_to="imagem_produto")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
# Create your models here.
