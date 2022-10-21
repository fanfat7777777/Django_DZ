from django import template
from django.utils.safestring import mark_safe

# template создаёт объект реестра тэгов и фильтров, через который 
# они будут проходить регистрацию для применения их в шаблоне
register = template.Library()

# декоратор 
# тэг или фильтр берёт имя функции(email_to_link) к которой применён декоратор
# У функции есть обязательный параметр value

# mark_safe указывает, что вёрстка безопасна и её можно использовать 
# внутри другой вёрстки
@register.filter
def email_to_link(value):
    return mark_safe(f"<a href='mailto:{value}'>{value}</a>")