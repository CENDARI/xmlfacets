from django.core.management.base import NoArgsCommand, CommandError
from django.utils.encoding import smart_str
from django.db import transaction
from lxml import etree
from os import path
from optparse import make_option
from xmlfacets.main.models import User, XMLDocument

import urllib2
import urllib
import json
import pprint
import datetime

import re

def read_cendari(apikey, url):
    request = urllib2.Request(url)
    request.add_header('Authorization', apikey)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        print e
        return None
    assert response.code == 200
    return response.read()

def read_cendari_json(apikey, data = '/dataspaces'):
    url = "http://134.76.21.222:8081/v1%s" % data
    response = read_cendari(apikey, url)
    if not response:
        return response
    response_dict = json.loads(response)
    return response_dict

class Command(NoArgsCommand):
    args = '<xml_filename xml_filename ...>'
    label = 'XML filename'
    help = 'Imports the specified XML files.'

    option_list = NoArgsCommand.option_list + (
        make_option('-u',
                    '--username',
                    action='store',
                    default='fekete',
                    help='username that will create/update documents'),
        make_option('-a',
                    '--apikey',
                    action='store',
                    default='',
                    help='API Key'),

        make_option('-f',
                    '--force-update',
                    action='store_true',
                    default=False,
                    help='update documents whether or not they have changed'),
    )
    def handle_noargs(self, **options):
        apikey = options['apikey']
        data = read_cendari_json(apikey)
        data = data['data']
        for r in data:
            if r['name'] == u'cendari-archival-descriptions':
                nextPage = r['resources']
                break
        else:
            raise CommandError("Cannot find archival descriptions")
        while nextPage:
            print "Accessing page %s" % nextPage.encode('utf-8')
            data = read_cendari_json(apikey, data=nextPage)
            if data is None:
                raise CommandError('Invalid nextPage URL %s' % nextPage)
            for label in data['data']:
                try:
                    self.do_label(label, options)
                except CommandError as e:
                    print e
            nextPage = data['nextPage']

    def do_label(self, entry, options):
        apikey = options['apikey']

        if not 'format' in entry:
            raise CommandError('No format in entry.')
        if entry['format'] != 'xml':
            return

        if not 'size' in entry:
            raise CommandError('No size in entry.')
        if entry['size'] == 0:
            return

        if not 'modified' in entry:
            raise CommandError('No modified time in entry.')
        last_updated = datetime.datetime.fromtimestamp(entry['modified']/1000)

        if not 'name' in entry:
            raise CommandError('No name in entry.')
        filename = entry['name']

        if not 'dataUrl' in entry:
            raise CommandError('No dataUrl in entry.')
        dataUrl = entry['dataUrl']

        if not options['force_update'] and XMLDocument.objects.filter(filename=filename).filter(last_updated__gte=last_updated):
            print "Skiping %s" % filename.encode('utf-8')
            return

        try:
            xml = read_cendari(apikey, dataUrl)
            root = etree.fromstring(xml)
        except etree.LxmlError as e:
            raise CommandError('could not parse %s:\n  %s' % (dataUrl, e))
        
        self.handle_xml(filename, last_updated, root, **options)

    @transaction.commit_on_success
    def handle_xml(self, filename, last_updated, root, **options):
        try:
            user = User.objects.get(username=options['username'])
        except User.DoesNotExist:
            raise CommandError('unknown user: %s' % options['username'])
        pis = {}
        pi = root.getprevious()
        while pi is not None:
            if isinstance(pi, etree._ProcessingInstruction):
                pis[pi.target] = pi.attrib
            pi = pi.getprevious()

        contents = etree.tostring(root, encoding=unicode)

        document, created = XMLDocument.objects.get_or_create(
            filename=filename, 
            defaults={ 'creator': user,
                       'last_updated': last_updated,
                       'last_updater': user,
                       'contents': contents })
        if not created:
            print "Replacing %s" % filename.encode('utf-8')
            document.contents = contents
            document.last_updater = user
            document.last_updated = last_updated
        else:
            print "Creating  %s" % filename.encode('utf-8')

        if 'xml-document' in pis:
            document.schema = pis['xml-document']['href']
        else:
            document.schema = None

        if 'xml-stylesheet' in pis:
            document.stylesheet = pis['xml-stylesheet']['href']
        else:
            document.stylesheet = None
        document.save()
        print filename.encode('utf-8'), "imported"
