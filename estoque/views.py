from django.shortcuts import render
from .forms import ProdutoForm
from .models import Categoria,Produto,Imagem
from django.http import HttpResponse
from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('cadastrar_produtos')
def add_produto(request):
    if request.method == "GET":
        ean = request.GET.get('ean')
        descricao = request.GET.get('descricao')
        categoria = request.GET.get('categoria')
        produtos_tab = Produto.objects.all()

        if ean or descricao or categoria:
            if ean:
                produtos_tab = produtos_tab.filter(ean=ean)
            if descricao:
                produtos_tab = produtos_tab.filter(descricao__icontains=descricao)
             

        categorias = Categoria.objects.all()
        return render(request, 'add_produto.html', 
                        {'categorias': categorias, 'produtos_tab': produtos_tab})
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
            messages.add_message(request, 
                        messages.SUCCESS, 'Produto cadastrado com sucesso!')
        return redirect(reverse('add_produto'))

def produto(request, slug):
    if request.method == "GET":
        produto = Produto.objects.get(slug=slug)
        data = produto.__dict__
        data['categoria'] = produto.categoria.id
        form = ProdutoForm(initial=data)
        return render(request, 'produto.html', {'form': form})
    

# Create your views here.