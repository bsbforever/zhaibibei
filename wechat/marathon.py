#coding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import re
def get_matchlist(month):
    match_list=[]
    p = re.compile(r'\d+')
    url='http://www.runchina.org.cn/portal.php?mod=calendar&ac=list&year=2017&month='+month+'&project=0'
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
	date=p.findall(match_date)
        length=len(date)
	if length==2:
	    match_date=date[0]+date[1]+'00'
	else:
	    match_date=date[0]+date[1]+date[2]
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
if __name__=="__main__":
    result=get_matchlist()
    for i in result:
        print (i['match_address'])
