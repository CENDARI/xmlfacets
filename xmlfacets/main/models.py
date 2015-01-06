# -*- coding: utf-8 -*-

import fields
import json
import re

from lxml import etree

from django.db import models
from django.contrib.auth.models import User, Group

from django.core import urlresolvers
from django.core.exceptions import ValidationError
from django.core.urlresolvers import NoReverseMatch
from django.utils.html import conditional_escape, escape
from django.utils.safestring import mark_safe

class Person(models.Model):
    name = models.CharField(max_length=1024,null=True)
    email = models.EmailField(null=True)
    user = models.ForeignKey(User, editable=False, null=True)

class Date(models.Model):
    last_updated = models.DateTimeField(primary_key=True)

class Event(models.Model):
    event = models.CharField(max_length=1024,primary_key=True)

class Format(models.Model):
    format = models.CharField(max_length=1024,primary_key=True)

class Language(models.Model):
    lang = models.CharField(max_length=1024,primary_key=True)

class Organization(models.Model):
    org = models.CharField(max_length=1024,primary_key=True)

class Place(models.Model):
    location = models.CharField(max_length=1024,blank=True,null=True) # should be geo
    name = models.CharField(max_length=1024,blank=True,null=True)

class Publisher(models.Model):
    name = models.CharField(max_length=1024,primary_key=True)
    canonical = models.ForeignKey('self',editable=False,null=True)

class Reference(models.Model):
    name = models.CharField(max_length=1024,primary_key=True)

class Tag(models.Model):
    name = models.CharField(max_length=1024,primary_key=True)

class Document(models.Model):
    uri = models.URLField(primary_key=True)
    application = models.CharField(max_length=1024)
    artifact = models.CharField(max_length=1024)
    contributor = models.ManyToManyField(User, related_name='contr')
    creator = models.ForeignKey(User, editable=False, related_name='creator')
    date = models.ManyToManyField(Date)
    lang = models.ManyToManyField(Language)
    length = models.PositiveIntegerField(blank=True,null=True)
    org = models.ManyToManyField(Organization)
    person = models.ManyToManyField(Person, related_name='pers')
    place = models.ManyToManyField(Place)
    publisher = models.ManyToManyField(Publisher)
    ref = models.ManyToManyField(Reference)
    tag = models.ManyToManyField(Tag)
    text = models.TextField()
    title = models.CharField(max_length=1024)
    groups_allowed = models.ManyToManyField(Group, "ga+")
    users_allowed = models.ManyToManyField(User, "ga+")

class XMLDocument(models.Model):
    creator = models.ForeignKey(User, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updater = models.ForeignKey(User, editable=False, related_name='last_to_update_%(class)s_set')
    last_updated = models.DateTimeField(auto_now=True)    
    filename = models.CharField(max_length=1024,unique=True)
    contents = fields.XMLField()
    schema = models.CharField(max_length=128,null=True)
    stylesheet = models.CharField(max_length=128,null=True)

    def get_creatorname(self):
        return self.creator.username

    @models.permalink
    def get_absolute_url(self):
        return ('document_view', [str(self.id)])
    def __unicode__(self):
        return self.filename
