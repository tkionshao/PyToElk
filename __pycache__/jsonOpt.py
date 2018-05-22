import json
import pprint
import datetime
with open("kate_customers.json") as a:
    b = json.load(a)
tag = b[2]['下單日期']
print("Before: ",tag)
print("Type, before:",type(tag))
tag = datetime.datetime.strptime(tag, '%Y/%m/%d').date()
b[2]['下單日期'] = tag
print("After: ",b[2]['下單日期'])
print("Type, after:",type(b[2]['下單日期']))
# datetime.strptime("24052010", "%d%m%Y").date()
# pprint.pprint("This is ",str(tag))
# print("tag is ",tag)
# print("tag is a ",type(b))
# print("Type of tag is ",type(tag))
# pprint.pprint(b)
