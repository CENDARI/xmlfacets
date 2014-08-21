#!/bin/sh

curl -XGET 'http://127.0.0.1:9200/cendari/document/_search?pretty' -d '@cendari_search.json' 
