# -*- coding: utf-8 -*-

import os.path
import re
import unicodedata
import urllib2
import urllib
import json

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

def geocode(address,locality=None,country=None,postal_code=None):
    mapsKey = settings.GOOGLE_GEOCODE_API_KEY
    mapsUrl = 'https://maps.googleapis.com/maps/api/geocode/json?sensor=false&address='
#    pdb.set_trace()
    if address is None:
        address = ''
    # This joins the parts of the URL together into one string.
    url = ''.join([mapsUrl,urllib.quote(address.encode('utf-8')), '&key=',mapsKey])
    if locality or country or postal_code:
        url += "&components="
    if locality:
        url = url + "locality:" + urllib.quote(locality.encode('utf-8'))
    if country:
        if locality:
            url += "|"
        url += "country:" + urllib.quote(country.encode('utf-8'))
    if postal_code:
        if locality or country:
            url += "|"
        url += "postal_code:" + urllib.quote(postal_code.encode('utf-8'))

    # This retrieves the URL from Google.
    data = urllib.urlopen(url).read()
    ret = json.loads(data)
    if ret['status'] != 'OK':
        print "Failed for url = %s with status %s" % (url, ret['status'])
        return None
    results = ret['results'][0]
    geometry = results['geometry']['location']
    return [ geometry['lat'], geometry['lng'] ]

