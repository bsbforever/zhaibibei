#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
#get movie douban Link

def douban(moviename):
    url='https://movie.douban.com/subject_search?search_text='+moviename+'&cat=1002'
    r=requests.get(url)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    try:
        douban=soup.find('a',attrs = {'class' : 'nbg'})
        link=douban['href']
        title=douban['title']
    except Exception as e:
	result='未找到相关影片'
	return result
    #get moive info
    r=requests.get(link)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    try:
        rank=soup.find('strong',attrs = {'class' : 'll rating_num'}).text
        summary=soup.find('span',attrs = {'property' : 'v:summary'}).text.strip()
	rank_summary=str(rank)+'\n'+summary
    except Exception as  e:
        rank_summary=''

    result=title+'\n'+rank_summary
    return result
    #return summary
#print soup

def panc(moviename):
    #moviename='西部世界'
    #nameurl=urllib.quote(moviename)
    url='http://www.panc.cc/s/'+moviename+'/td_0'
    r=requests.get(url)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    result=soup.find_all('div',attrs = {'class' : 'aw-item active'})
    movielist=[]
    for i in result:
        name=i.h1.text
        link=str(i.h1.find('a',attrs = {'rel' : 'noreferrer'})['href'])
        #link=link.replace('amp;','')
	#link=URLEncoder.Encode(link)
        movielist.append(name+' : '+link)
    movielist='\n'.join(movielist)
    return movielist

if __name__=="__main__":
    moviename='西部世界'
    print panc(moviename)
