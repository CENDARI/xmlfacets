from django.core.management.base import BaseCommand, CommandError
from django.utils.encoding import smart_str
from django.db import transaction
from lxml import etree
from os import path
from optparse import make_option
from xmlfacets.main.models import User, XMLDocument

import re

class Command(BaseCommand):
    args = '<xml_filename xml_filename ...>'
    label = 'XML filename'
    help = 'Imports the specified XML files.'

    option_list = BaseCommand.option_list + (
        make_option('-u',
                    '--username',
                    action='store',
                    default='fekete',
                    help='username that will create/update documents'),
        make_option('-p',
                    '--prefix',
                    action='store',
                    default='',
                    help='Prefix to remove from file name'),

        make_option('-f',
                    '--force-update',
                    action='store_true',
                    default=False,
                    help='update documents whether or not they have changed'),
    )
    def handle(self, *labels, **options):
        for label in labels:
            try:
                self.do_label(label, options)
            except CommandError as e:
                print e

    def do_label(self, filename, options):
        if not path.isfile(filename):
            raise CommandError('%s is not a file.' % filename)

        if filename.startswith(options['prefix']):
            sfilename = filename[len(options['prefix']):]
        if not options['force_update'] and XMLDocument.objects.filter(filename=sfilename):
            print "Skiping %s" % sfilename
            return

        try:
            doc = etree.parse(filename)
        except etree.LxmlError as e:
            raise CommandError('could not parse %s:\n  %s' % (filename, e))
        
        self.handle_xml(sfilename, doc, **options)

    @transaction.commit_on_success
    def handle_xml(self, filename, doc, **options):
        try:
            user = User.objects.get(username=options['username'])
        except User.DoesNotExist:
            raise CommandError('unknown user: %s' % options['username'])
        pis = {}
        pi = doc.getroot().getprevious()
        while pi is not None:
            if isinstance(pi, etree._ProcessingInstruction):
                pis[pi.target] = pi.attrib
            pi = pi.getprevious()

        contents = etree.tostring(doc, encoding=unicode)

        document, created = XMLDocument.objects.get_or_create(
            filename=filename, 
            defaults={ 'creator': user,
                       'last_updater': user,
                       'contents': contents })
        if not created:
            print "Replacing %s" % filename
            document.contents = contents
            document.last_updater = user
        else:
            print "Creating  %s" % filename

        if 'xml-document' in pis:
            document.schema = pis['xml-document']['href']
        else:
            document.schema = None

        if 'xml-stylesheet' in pis:
            document.stylesheet = pis['xml-stylesheet']['href']
        else:
            document.stylesheet = None
        document.save()
        print filename, "imported"
