from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, Context

from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView
from haystack.inputs import Raw

from templatetags.display import as_xml


from models import *

# Create your views here.

class XMLDocumentList(ListView):
    model = XMLDocument
    context_object_name = "xmldocument_list"
    template_name = "xmldocument_list.html"
    queryset = XMLDocument.objects.order_by('filename')

#def index(request):
#    return HttpResponse('Hello, %d documents indexed' % XMLDocument.objects.count())


sqs = SearchQuerySet()
sqs = sqs.facet('contributor')
sqs = sqs.facet('coverage')
sqs = sqs.facet('creator')
sqs = sqs.facet('application')
sqs = sqs.facet('date')
sqs = sqs.facet('format')
sqs = sqs.facet('languages')
sqs = sqs.facet('publisher')
sqs = sqs.facet('countries')
sqs = sqs.facet('themes')
sqs = sqs.facet('firsttag')
sqs = sqs.facet('schema')
sqs = sqs.facet('places')
sqs = sqs.facet('events')
sqs = sqs.facet('persons')
sqs = sqs.facet('tags')
sqs = sqs.facet('organizations')
sqs = sqs.facet('artifacts')
sqs = sqs.facet('references')
#sqs = sqs.facet('location', precision=3)
#sqs = sqs.filter(location=Raw('{"aggregations": { "lg": { "geohash_grid": { "field": "location", "precision": 3}}}}'))


class XMLFacetedSearchForm(FacetedSearchForm):
    def no_query_found(self):
        return self.searchqueryset.all()

class XMLFacetedSearchView(FacetedSearchView):
    searchqueryset=sqs
    def __init__(self, *args, **kwargs):
        if kwargs.get('searchqueryset') is None:
            kwargs['searchqueryset'] = sqs
        if kwargs.get('form_class') is None:
            kwargs['form_class'] = XMLFacetedSearchForm
        super(XMLFacetedSearchView, self).__init__(*args, **kwargs)

    def create_response(self):
        if not self.request.META.get('QUERY_STRING', ''):
            print "Patching QUERY_STRING"
            self.request.META['QUERY_STRING']="q="

        return super(XMLFacetedSearchView, self).create_response()

    def extra_context_(self):
        extra = super(XMLFacetedSearchView, self).extra_context()
        print self.results
        if self.query == '':
            extra['facets'] = sqs.facet_counts()
        return extra

def document(request, document_id):
    xmldocument = get_object_or_404(XMLDocument, pk=document_id)
    return render(request, 'main/xmldocument.html', {'xmldocument': xmldocument})

def download(request, document_id):
    xmldocument = get_object_or_404(XMLDocument, pk=document_id)
    filename = xmldocument.filename.rsplit("/")[-1]
    response = HttpResponse(content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename

    response.write(as_xml(xmldocument.contents))
    return response
