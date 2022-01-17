from django import template

register = template.Library()


@register.simple_tag
def get_lang_url(request, lang):
    url = request.path.split('/')
    url[1] = lang
    url = '/'.join(url)
    return url


@register.simple_tag()
def get_price_url(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'  ## nimaga null java script null
