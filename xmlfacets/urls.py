from django.conf.urls import patterns, include, url

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
    url(r'^$', 'index', name='index'),
    url(r'^search$', 'search', name='index'),
    url(r'^document/(?P<document_id>\d+)/$', 'document', name='document_view'),
    url(r'^download/(?P<document_id>\d+)/$', 'download', name='download_xml'),
)

