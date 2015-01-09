from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, Context

from templatetags.display import as_xml

from elastic import *
from models import *

# Create your views here.

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
    terms = {}
    if 'selected_facets' in request.GET and request.GET['selected_facets']:
        facets=request.GET.getlist('selected_facets');
        for facet in facets:
            (facet,value) =facet.split(':')
            if facet in terms:
                terms[facet].append(value)
            else:
                terms[facet] = [value]
        and_terms = [{"terms": {key: val}} for (key, val) in terms.items()]
        if len(and_terms) == 1:
            q = q.filter_raw(and_terms[0])
        else:
            q = q.filter_raw({'and': and_terms})
    res = q.execute()
    o={'res': res, 'query': query, 'request': request, 'selected_facets': terms}
    return render(request, 'search/cendarisearch.html', o)

# def document(request, document_id):
#     xmldocument = get_object_or_404(XMLDocument, pk=document_id)
#     return render(request, 'main/xmldocument.html', {'xmldocument': xmldocument})

# def download(request, document_id):
#     xmldocument = get_object_or_404(XMLDocument, pk=document_id)
#     filename = xmldocument.filename.rsplit("/")[-1]
#     response = HttpResponse(content_type='text/xml')
#     response['Content-Disposition'] = 'attachment; filename="%s"' % filename

#     response.write(as_xml(xmldocument.contents))
#     return response
