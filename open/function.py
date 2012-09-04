# coding=UTF-8
import re
import math
import time

def Average(datalist):
    r=0
    for i in datalist:
        r+=i
    result=float(r)/len(datalist)
    if result<10:
        result=round(result,1)
    else:
        result=int(result)
    return result

def Normalprice(price=None):
    #resource_price=re.search('\d+(\.\d+)?',str(price))
    #if resource_price is not None:
        #friendly_price=float(resource_price.group())
        #normal_price=int(friendly_price)
        #return normal_price
    #else:
        #return
    if price is None:
        return ''
    if price>=10000:
        if round(price/10000,1)==int(price/10000):
           return '￥'+str(int(price/10000))+'万'
        else:
           return '￥'+str(round(price/10000,1))+'万'
    elif price>=100:
        return '￥'+str(int(price))
    else:
        return '￥'+str(price)

def Normaltime(date=None):
    if date is None:
        return ''
    from_format='%Y-%m-%d %H:%M:%S'
    to_format='%Y年%m月%d日'
    date=str(date)
    date=time.strftime(to_format,time.strptime(date,from_format))
    return date
   
def Normdistribution(x,u=0,sigma=0.4):
    x=float(x)/200
    u=float(u)/200
    pai=3.141592653
    e=2.718281828
    index=-pow((x-u),2)/(2*pow(sigma,2))
    result=1/(sigma*math.sqrt(2*pai))*pow(e,index)
    result=180*result
    return result