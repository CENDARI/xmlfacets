from django.contrib import admin
from models import XMLDocument

class XMLDocumentAdmin(admin.ModelAdmin):
    readonly_fields = ( 'creator', 'created', 'last_updater', 'last_updated')
    list_display = ('filename', 'schema', 'stylesheet' )
#    fields = ('filename', 'schema', 'stylesheet', 'contents' )

admin.site.register(XMLDocument, XMLDocumentAdmin)
