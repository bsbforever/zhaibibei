__author__ = 'bsbfo'
#coding=utf-8
from bs4 import BeautifulSoup
import requests
import time

def get_matchlist():
    match_list=[]

    url='http://www.runchina.org.cn/portal.php?mod=calendar&ac=list&year=2017&month=04&project=0'
    r=requests.get(url)

    content=r.content
    soup = BeautifulSoup(content,"lxml")
    match=soup.find_all('ul',attrs = {'class' : 'match-list'})
    match=match[0]
    match_item=match.find_all('div',attrs = {'class' : 'match-item'})
    for i in match_item:
        match_dic={}
        match_name=i.find('span',attrs = {'class' : 'match-name text-omit'}).text.strip()
        match_info=i.find_all('span',attrs = {'class' : 'match-info text-omit'})
        match_address=match_info[0].text.strip()
        match_date=match_info[1].text.strip()
        match_website=i.find('a')['href']
        match_distance=match_info[3].text.strip()
        match_count=match_info[4].text.strip()
        match_detail='http://www.runchina.org.cn/'+i.find('a',attrs = {'class' : 'match-link'})['href']
        match_dic['match_name']=match_name
        match_dic['match_address']=match_address
        match_dic['match_date']=match_date
        match_dic['match_website']=match_website
        match_dic['match_count']=match_count
        match_dic['match_detail']=match_detail
        match_list.append(match_dic)
    return match_list

def get_lyric():
    match_list=[]

    url='https://genius.com/Jay-z-holy-grail-lyrics'
    r=requests.get(url)

    content=r.content
    #print (content)
    soup = BeautifulSoup(content,"lxml")
    #match=soup.find_all('section')
    lyric=soup.find_all('div',attrs = {'class' : 'song_body-lyrics'})[0].text
    #match=soup.find_all('div',attrs = {'class' : 'lyrics'})
    return lyric


result=get_lyric()
print (result)

