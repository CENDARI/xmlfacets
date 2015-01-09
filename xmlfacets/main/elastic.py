from django.conf import settings
from elasticutils import S

import json


#import elasticutils.contrib.django
#import elasticutils.MappingType


CENDARI_FACETS = [
    "application",
    "artifact",
    "contributor",
    "creator",
    "event",
    "format",
    "language",
    "org",
    "person",
    "place",
    "publisher",
    "ref",
    "tag",
]

def cendariS():
    return S().es(urls=settings.ES_URLS).indexes('cendari').doctypes('document')

def cendariFacets(S,size=10):
    return S.facet(*CENDARI_FACETS,size=size,filtered=True)

def cendariTest():
    return cendariFacets(cendariS())
