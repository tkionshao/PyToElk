from elasticsearch import Elasticsearch
import json
import time
import datetime
import dateTransform
import pprint
import random
es = Elasticsearch()

with open("kate_customers.json") as a:
    b = json.load(a)
tag = b[4]
# print(tag)
# dateTransform.dateTransform(b)
#pprint.pprint(b)

# Testing
# es.indices.create(index='test1-index', ignore=400)
# res = es.index(index="test1-index", doc_type='testfile', id=199, body=tag)
i = 0
while True:
    body={"sensor": random.randint(100,9999),"user":"user"+str(i) ,"timestamp": datetime.datetime.now(),"status":"happy"}
    res = es.index(index="test2-index", doc_type="test-type", body=body)
    print(res["result"])
    time.sleep(1)

    # a = es.get(index="test-index", doc_type="test-type", id=i)
    # print(type(a))
    # print(a["any"])
    i += 1
    print(i)

'''
print("b is a ",type(b))
print("Something inside b is a ",type(b[1]))

for i in range(1,len(b)):
    res = es.index(index="cat3-index", doc_type='tweet', id=i, body=b[i-1])
    print(res['result'])
    res = es.get(index="cat3-index", doc_type='tweet', id=i)
    print(res['_source'])
    print(i,len(b))
    time.sleep(1)
'''
# for index in es.indices.get('*'):
#   pprint.pprint(index)
