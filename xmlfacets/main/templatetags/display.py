from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from lxml import etree

from xmlfacets.main.utils import xml_to_text

register = template.Library()

@register.filter
def as_text(tree):
    return xml_to_text(tree)

@register.filter
def as_xml(tree):
    if tree is None:
        return ''
    return mark_safe(etree.tostring(tree))
