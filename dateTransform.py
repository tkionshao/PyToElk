
import datetime
def dateTransform(b):
    for i in range(len(b)):
        tag = b[i]['下單日期']
        try:
            #print("Before: ",b[i]['下單日期'])
            #print("Type, before:",type(tag))
            tag = datetime.datetime.strptime(tag, '%Y/%m/%d').date()
            b[i]['下單日期'] = tag
            print("After: ",b[i]['下單日期'])
            print(tag)
            #print("Type, after:",type(b[i]['下單日期']))
        except:
            b[i]['下單日期'] = datetime.datetime.now().date()
