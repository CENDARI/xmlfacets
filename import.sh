#!/bin/sh

find $1 -name '*.xml' -print0 | xargs -0 bin/python manage.py import -u "$2" -p $1 
