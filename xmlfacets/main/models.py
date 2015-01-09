# -*- coding: utf-8 -*-

# import fields
# import json
# import re

# from lxml import etree

# from django.db import models
# from django.contrib.auth.models import User, Group

# from django.core import urlresolvers
# from django.core.exceptions import ValidationError
# from django.core.urlresolvers import NoReverseMatch
# from django.utils.html import conditional_escape, escape
# from django.utils.safestring import mark_safe

# class XMLDocument(models.Model):
#     creator = models.ForeignKey(User, editable=False)
#     created = models.DateTimeField(auto_now_add=True)
#     last_updater = models.ForeignKey(User, editable=False, related_name='last_to_update_%(class)s_set')
#     last_updated = models.DateTimeField(auto_now=True)    
#     filename = models.CharField(max_length=1024,unique=True)
#     contents = fields.XMLField()
#     schema = models.CharField(max_length=128,null=True)
#     stylesheet = models.CharField(max_length=128,null=True)

#     def get_creatorname(self):
#         return self.creator.username

#     @models.permalink
#     def get_absolute_url(self):
#         return ('document_view', [str(self.id)])
#     def __unicode__(self):
#         return self.filename
