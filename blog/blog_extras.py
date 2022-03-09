from django import template

register = template.Library()


@register.simple_tag
def row():
    return '<div class="row">'


@register.simple_tag
def endrow():
    return "</div>"

