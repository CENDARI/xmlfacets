from django.conf.urls import patterns, include, url

from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView

sqs = SearchQuerySet()
sqs = sqs.facet('firsttag')
# sqs.facet('creator')
sqs = sqs.facet('languages')

from main.views import XMLDocumentList, XMLFacetedSearchView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xmlfacets.views.home', name='home'),
    # url(r'^xmlfacets/', include('xmlfacets.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('xmlfacets.main.views',
#    url(r'^$', 'index', name='index'),
#    url(r'^$', XMLDocumentList.as_view(), name='index'),
    url(r'^document/(?P<document_id>\d+)/$', 'document', name='document_view'),
    url(r'^$', XMLFacetedSearchView(), name='haystack_search2'),
#    url(r'^search/$', FacetedSearchView(form_class=FacetedSearchForm, searchqueryset=sqs), name='haystack_search'),
#    url(r'^search/$', 'basic_search', name='haystack_search'),
    url(r'^download/(?P<document_id>\d+)/$', 'download', name='download_xml'),
)

