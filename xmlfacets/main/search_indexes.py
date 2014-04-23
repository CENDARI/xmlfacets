# -*- coding: utf-8 -*-

#from haystack import site
from haystack.indexes import *
from django.db.models.fields import FieldDoesNotExist
from models import XMLDocument
from utils import geocode
import json

import pdb

class XMLDocumentIndex(SearchIndex, Indexable):
    text = CharField(document=True, use_template=True)
    created = DateTimeField(model_attr='created')
    creator = CharField(faceted=True)
    schema = CharField(model_attr='schema', faceted=True,null=True)
    languages = MultiValueField(faceted=True)
    firsttag = CharField(faceted=True)
    themes = MultiValueField(faceted=True)
    countries = MultiValueField(faceted=True)
    affiliations = MultiValueField(faceted=True)
    location = LocationField()

    def get_model(self):
        return XMLDocument
        
    def index_queryset(self, using=None):
        return self.get_model().objects

    def prepare_creator(self, obj):
        return obj.creator.username

    def prepare_languages(self, obj):
        s = set(obj.contents.xpath('//@xml:lang'))
        if '' in s:
            s.remove('')
        if not s:
            s.add('none')
        return s

    def prepare_firsttag(self, obj):
        return obj.contents.tag.rsplit("}", 1)[-1]

    def prepare_themes(self, obj):
        themes = []
        if None in obj.contents.nsmap:
            ns={'t': obj.contents.nsmap[None]}
            themes = obj.contents.xpath("//t:controlaccess[t:head='Theme']/t:subject", namespaces=ns)
        else:
            themes = obj.contents.xpath("//controlaccess[/head='Theme']/subject")
        if themes:
            return [t.text for t in themes]

    def prepare_countries(self, obj):
        countries = []
        if None in obj.contents.nsmap:
            ns={'t': obj.contents.nsmap[None]}
            countries = obj.contents.xpath("//t:country", namespaces=ns)
        else:
            countries = obj.contents.xpath("//country")
        if countries:
            return [c.text for c in countries]

    def prepare_affiliations(self, obj):
        affiliations = []
        ns={ 't': 'http://www.tei-c.org/ns/1.0'}
        affiliations = obj.contents.xpath("//t:affiliation/t:orgName[@type='institution']", namespaces=ns)
        if affiliations:
            return [t.text for t in affiliations]

    def prepare_location(self, obj):
        url = ''
        if None in obj.contents.nsmap:
            url = obj.contents.nsmap[None]
            ns={'t': url}
            locations = obj.contents.xpath("//t:desc/t:location", namespaces=ns)
        else:
            locations = obj.contents.xpath("//desc/location")
#        pdb.set_trace()
        if locations:
            l = locations[0]
            address = ' '.join([e.text or '' for e in l.iter()])

            loc = geocode(address)

            if loc:
                return "%s,%s" % (loc[0], loc[1])
        return None
