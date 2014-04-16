# -*- coding: utf-8 -*-

#from haystack import site
from haystack.indexes import *
from django.db.models.fields import FieldDoesNotExist
from models import XMLDocument
import json

class XMLDocumentIndex(SearchIndex, Indexable):
    text = CharField(document=True, use_template=True)
    created = DateTimeField(model_attr='created')
    creator = CharField(faceted=True)
    schema = CharField(model_attr='schema', faceted=True,null=True)
    languages = MultiValueField(faceted=True)
    firsttag = CharField(faceted=True)

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
