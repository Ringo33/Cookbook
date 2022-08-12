from django import template
from django.utils.text import slugify
from transliterate import translit

register = template.Library()


@register.filter
def slug_transl(field):
    result = slugify(translit(str(field), language_code='ru', reversed=True))
    return result

@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})