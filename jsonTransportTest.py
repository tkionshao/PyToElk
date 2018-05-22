from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

import json
jj = open('kate_customers.json')
list = json.load(jj)
res = es.bulk(index="cat-index",  body=list)
print(res['result'])


j = 0
actions = []
while (j <= 10):
    action = {
        "_index": "tickets-index",
        "_type": "tickets",
        "_id": j,
        "_source": {
            "any":"data" + str(j),
            "timestamp": datetime.now()
            }
        }
    actions.append(action)
    j += 1

helpers.bulk(es, actions)
'''
    res = es.get(index="test-index", doc_type='tweet', id=1)
    print(res['_source'])

es.indices.refresh(index="cat-test")
'''
'''
res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
'''
