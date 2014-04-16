# -*- coding: utf-8 -*-

import re
from django import forms
from django.db import models
from lxml import etree
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode

def update_attrs(attrs, extra_attrs):
    if attrs is None:
        attrs = extra_attrs
    else:
        for k, v in extra_attrs.iteritems():
            if k in attrs and k in ['class', 'style']:
                values = attrs[k].split()
                values.extend(extra_attrs[k].split())
                if k == 'class':
                    attrs[k] = ' '.join(values)
                elif k == 'style':
                    attrs[k] = '; '.join(values)
            else:
                attrs[k] = extra_attrs[k]

class XMLWidget(forms.Textarea):
    def _format_value(self, value):
        if value is None:
            return ''
        if isinstance(value, etree._Element):
            return etree.tostring(value, encoding=unicode)
        if isinstance(value, str) or isinstance(value, unicode):
            return value
        raise TypeError('%s cannot be formatted as XML' % value)
    def render(self, name, value, attrs=None):
        update_attrs(attrs, { 'class': 'xml-textarea' })
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(u'<textarea%s>%s</textarea>' % (
                forms.util.flatatt(final_attrs),
                conditional_escape(force_unicode(self._format_value(value)))))

class ReadonlyXMLWidget(XMLWidget):
    def render(self, name, value, attrs=None):
        update_attrs(
            attrs, { 'style': 'display: none', 'class': 'hidden-textarea' })
        return (mark_safe(
                '<div class="readonly">' 
                + self._format_value(value)
                + '</div>') 
                + super(ReadonlyXMLWidget, self).render(name, value, attrs))

class XMLField(models.Field):
    description = 'A parsed XML fragment'
    __metaclass__ = models.SubfieldBase
    def __init__(self, *args, **kwargs):
        super(XMLField, self).__init__(*args, **kwargs)
    def db_type(self, connection):
        return 'xml'
    def to_python(self, value):
        if value is None:
            return None
        if isinstance(value, etree._Element):
            return value
        if not (isinstance(value, str) or isinstance(value, unicode)):
            raise TypeError('%s cannot be parsed to XML' % type(value))
        if len(value) == 0 or value == '<br/>':
            return None
        # strip out entity-encoded carriage returns (pasted MS Word garbage)
        value = re.sub(r'(&#13;\n)+', ' ', value)
        fragment = None
        try:
            fragment = etree.fromstring(value)  # FIX
        except etree.ParserError:
            fragment = etree.fromstring('<div>'+value+'</div')
        return fragment 
    def get_prep_value(self, value):
        if value is None:
            return None
        else:
            return etree.tostring(value)
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)
    def formfield(self, **kwargs):
        defaults = {'widget': XMLWidget}
        defaults.update(kwargs)
        return super(XMLField, self).formfield(**defaults)


