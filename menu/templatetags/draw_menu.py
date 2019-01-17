from django import template
from menu.models import *

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html')
def draw_menu(menu):
    all_inner_options = {}
    selected_menu = Menu.objects.filter(title=menu).first()
    options = Option.objects.filter(menu=selected_menu)
    for option in options:
        inner_option = InnerOption.objects.filter(option=option)
        all_inner_options[option] = inner_option

    # чтобы сделать в один запрос - join

    return {'selected_menu': selected_menu, 'options': options, 'all_inner_options': all_inner_options}