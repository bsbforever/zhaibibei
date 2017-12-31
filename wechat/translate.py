#/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random

appKey = '1bd2b9b49704999b'
secretKey = '您的应用密钥'

 
httpClient = None
myurl = '/api'
q = 'good'
fromLang = 'EN'
toLang = 'zh-CHS'
salt = random.randint(1, 65536)

sign = appKey+q+str(salt)+secretKey
m1 = md5.new()
m1.update(sign)
sign = m1.hexdigest()
myurl = myurl+'?appKey='+appKey+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
try:
    httpClient = httplib.HTTPConnection('openapi.youdao.com')
    httpClient.request('GET', myurl)
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
				
