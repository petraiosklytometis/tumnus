from django.shortcuts import render
from .models import Categoria,Produto,Imagem
from django.http import HttpResponse
from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

def add_produto(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        return render(request, 'add_produto.html', 
                        {'categorias': categorias})
    elif request.method == "POST":
        descricao = request.POST.get('descricao')
        ean = request.POST.get('ean')
        sku = request.POST.get('sku')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        preco_custo = request.POST.get('preco_custo')
        # TODO: Fazer cálculo de preço por BinaryField
        preco_venda = request.POST.get('preco_venda')

        produto = Produto(descricao=descricao,
                          ean=ean, sku=sku, 
                          categoria_id=categoria,
                          quantidade=quantidade, 
                          preco_custo=preco_custo,
                          preco_venda=preco_venda)
        produto.save()

        for f in request.FILES.getlist('imagens'):
            name = f'{date.today()}-{produto.id}.jpg'

            img = Image.open(f)
            img = img.convert('RGB')
            img = img.resize((300,300))
            draw = ImageDraw.Draw(img)
            draw.text((20, 280), f"TUMNUS {date.today()}", (15, 109, 172))
            output = BytesIO()
            img.save(output, format='JPEG', quality=100)
            output.seek(0)
            img_final = InMemoryUploadedFile(output, 'ImageField',
                                            name, 'image/jpeg',
                                            sys.getsizeof(output),
                                            None
            )

            img_dg = Imagem(imagem = img_final, produto=produto)
            img_dg.save()
        return HttpResponse('Foi')

        
# Create your views here.