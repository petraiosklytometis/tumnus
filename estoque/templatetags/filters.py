from django import template
from estoque.models import Imagem

register = template.Library()

@register.filter(name='get_first_image')
def get_first_image(product):
    image = Imagem.objects.filter(produto=product).first()
    return image.imagem.url