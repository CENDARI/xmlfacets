from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, Context

from templatetags.display import as_xml

from elastic import *
from models import *

# Create your views here.

def index(request,filter=None):
    q=cendariS()
    if filter:
        q = q.filter(filter)
    q = cendariFacets(q)
    res = q.execute()
    return render(request, 'main/document_list.html', {'res': res})

def search(request,query=None,filter=None,facets=None):
    q=cendariS()
    if query:
        q=q.query(query)
    elif 'q' in request.GET and request.GET['q']:
        query=request.GET['q']
        q=q.query(text__query_string=request.GET['q'])
    else:
        query=''
    if filter:
        q = q.filter(filter)
    elif 'f' in request.GET:
        q=q.filter(request.GET['f'])
    else:
        filter=''
    q = cendariFacets(q)
    if 'selected_facets' in request.GET and request.GET['selected_facets']:
        (facet,value)=request.GET['selected_facets'].split(':')
        q = q.filter_raw({'term': {facet: value}})
    res = q.execute()
    o={'res': res, 'query': query, 'request': request}
    return render(request, 'search/cendarisearch.html', o)

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
