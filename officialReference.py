from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
    'autczczhor': 'kzxczimchy',
    'teczxczxxt': 'Elasticsearch: cool.cxzcxz bonsai cool.',
    'timesczxcztamp': datetime.now()
    }

print(type(doc))

res = es.index(index="test2-index", doc_type='tweet', id=1, body=doc)
print(res['result'])

res = es.get(index="test2-index", doc_type='tweet', id=1)
print(res['_source'])

es.indices.refresh(index="test2-index")

res = es.search(index="test2-index", body={"query": {"match_all": {}}})

print("Got %d Hits:" % res['hits']['total'])

for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
