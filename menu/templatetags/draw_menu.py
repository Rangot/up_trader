from django import template
from menu.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu):
    active_menu_option = None
    opened_menu_ids = None
    menu = Menu.objects.filter(title=menu).first()
    request_url = context['request'].path
    locale_context = {'menu': menu}
    try:
        request_id = request_url.split('/')[-2]
        if request_id:
            active_menu_option = Menu.objects.get(id=request_id)
    except ObjectDoesNotExist:
        raise Http404('Menu object does not exist')
    else:
        if active_menu_option:
            opened_menu_ids = active_menu_option.get_elder_ids() + [active_menu_option.id]
        locale_context['opened_menu_ids'] = opened_menu_ids
    return locale_context


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu_children(context, child_id):
    child = Menu.objects.filter(id=child_id).first()
    locale_context = {'menu': child}
    if 'opened_menu_ids' in context:
        locale_context['opened_menu_ids'] = context['opened_menu_ids']
    return locale_context

