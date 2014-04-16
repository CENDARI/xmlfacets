from django.shortcuts import render
from django.http import HttpResponse
from models import *

# Create your views here.

def index(request):
    return HttpResponse('Hello, %d documents indexed' % XMLDocument.objects.count())

def document(request, document_id):
    return HttpResponse("You're looking at XML Document %s." % document_id)
