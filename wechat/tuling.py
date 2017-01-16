#coding=utf8
import requests
from bs4 import BeautifulSoup
import random


def tuling1(info,userid):
    key='956fb8dabfb2453fa6abcb668d7e96a5'
    url='http://www.tuling123.com/openapi/api'
    #info='苏州'
    postdata={
        'key':key,
        'info':info,
	'userid':userid
             }

    r = requests.post(url, data = postdata)


    result=r.content

    result=eval(result)
    message_type= result['code']
    #print (message_type)
    #print type(message_type)
    if message_type==100000:
        tuling_reply={}
        tuling_reply['code']=(result['code'])
        tuling_reply['content']=(result['text']).strip()
        return tuling_reply
    if message_type==200000:
        #print (result['text'])
        #print (result['url'])
        tuling_reply={}
        tuling_reply['code'] = (result['code'])
        tuling_reply['description']=(result['text'])
        tuling_reply['title'] = (result['text'])
        tuling_reply['url'] = (result['url'])
        return tuling_reply
    if message_type==302000:
        tuling_reply={}
        tuling_reply['code'] = (result['code'])
        tuling_reply['text'] = (result['text'])
        news=result['list']
        tuling_reply['title1'] = news[0]['article']
        tuling_reply['picurl1'] = news[0]['icon']
        tuling_reply['description1'] = news[0]['source']
        tuling_reply['url1'] = news[0]['detailurl']
        tuling_reply['title2'] = news[1]['article']
        tuling_reply['picurl2'] = news[1]['icon']
        tuling_reply['description2'] = news[1]['source']
        tuling_reply['url2'] = news[1]['detailurl']
        return  tuling_reply

    if message_type==308000:
        tuling_reply={}
        tuling_reply['code'] = (result['code'])
        tuling_reply['text'] = (result['text'])
        caipu = result['list']
        tuling_reply['title1']=caipu[0]['name']
        tuling_reply['picurl1']=caipu[0]['icon']
        tuling_reply['description1'] = caipu[0]['info']
        tuling_reply['url1'] = caipu[0]['detailurl']
        tuling_reply['title2'] = caipu[1]['name']
        tuling_reply['picurl2'] = caipu[1]['icon']
        tuling_reply['description2'] = caipu[1]['info']
        tuling_reply['url2'] = caipu[1]['detailurl']
        tuling_reply['title3'] = caipu[2]['name']
        tuling_reply['picurl3'] = caipu[2]['icon']
        tuling_reply['description3'] = caipu[2]['info']
        tuling_reply['url3'] = caipu[2]['detailurl']
        tuling_reply['title4'] = caipu[3]['name']
        tuling_reply['picurl4'] = caipu[3]['icon']
        tuling_reply['description4'] = caipu[3]['info']
        tuling_reply['url4'] = caipu[3]['detailurl']
        return tuling_reply
if __name__=="__main__":
    info='王大可这个名字怎么样'
    userid='1234456'
    print tuling1(info,userid)

