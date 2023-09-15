from django import template
from estoque.models import Imagem

register = template.Library()

@register.filter(name='get_first_image')
def get_first_image(product):
    image = Imagem.objects.filter(produto=product).first()
    if image:
        return image.imagem.url
    else:
        return False