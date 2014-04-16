# -*- coding: utf-8 -*-

import os.path
import re
import unicodedata
from lxml import etree
from django.conf import settings
from django.utils.encoding import smart_text
import pdb

xslt = etree.parse(os.path.abspath(os.path.join(os.path.dirname(__file__), 'textify.xsl')))
textify = etree.XSLT(xslt)

def xml_to_text(xml):
    if xml is None: 
        return ''
#    pdb.set_trace()
    trans = textify(xml)
    string = unicode(trans) # etree.tostring(trans, method='text', encoding=unicode)
    if string is None:
        return ''
    return string.strip()

def truncate(text, length=120):
    if len(text) <= length:
        return text
    l = text[:(length/2)].rsplit(' ', 1)[0]
    r = text[-(length/2):].split(' ', 1)
    if len(r) == 1:
        r = r[0]
    else:
        r = r[1]
    return l + u'... ' + r

