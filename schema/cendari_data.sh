#!/bin/sh

curl -XDELETE 'http://localhost:9200/cendari/document/'
i=1
for f in cendari_data*.json
do
    curl -XPUT "http://localhost:9200/cendari/document/$i?pretty" -d '@'$f
    i=`expr $i + 1`
done
