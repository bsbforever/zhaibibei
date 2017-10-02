# -*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import selenium.webdriver
from selenium import webdriver
def cnbeta():
    url='http://www.cnbeta.com/top10.htm'
    r = requests.get(url)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    #print (soup)
    print ('一周热门新闻')
    print ('\n')
    counter_news1=soup.find_all('div',attrs = {'class' : 'cnbeta-update-list rank-list category-update counter_news'})[0]
    counter_news=counter_news1.find_all('div',attrs = {'class' : 'item'})
    for i in counter_news:
        try:
            #print (i)
            counter_title=i.find('dt').text
            #counter_content=i.find('dd').text
            counter_link=i.find('a')['href']

            print (counter_title)
            #print (counter_content)
            #print (counter_link)
            #break
            #print (all_game)
            #print (game_link)
            #print (game_title)
            #print (picture)
            #print (game_count)
            #print ('\n')
            #break
        except Exception as e:
            print (e)
    '''
    print ('一周热门评论新闻')
    print ('\n')
    comments_news1=soup.find_all('div',attrs = {'class' : 'cnbeta-update-list rank-list category-update comments_news'})[0]
    comments_news=comments_news1.find_all('div',attrs = {'class' : 'item'})
    for i in comments_news:
        try:
            #print (i)
            comments_title=i.find('dt').text
            #comments_content=i.find('dd').text
            comments_link=i.find('a')['href']

            print (comments_title)
            #print (comments_content)
            #print (comments_link)
            #break
            #print (all_game)
            #print (game_link)
            #print (game_title)
            #print (picture)
            #print (game_count)
            #print ('\n')
            #break
        except Exception as e:
            print (e)
def cnbeta_tech():
    url='http://www.cnbeta.com'
    r = requests.get(url)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    #print (soup)
    print ('\n')
    print ('最新科技新闻')
    print ('\n')
    tech_news=soup.find_all('div',attrs = {'class' : 'cb-group-carousel-inner'})
    for i in tech_news:
        try:
            tech_title=i.find('h2').text
   
            print (tech_title)
 
            #print ('\n')
            #break
        except Exception as e:
            print (e)

'''

def toutiao():
   
    r=requests.get('http://www.toutiao.com/api/pc/focus/')

    content=r.content
    content1=json.loads(content.decode())

    result= content1['message']

    data= content1['data']['pc_feed_focus']

    for i in data:
        print (i['title'])



def weibo():
    game_list=[]
    #driver = selenium.webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver = selenium.webdriver.PhantomJS()
    url=r'http://s.weibo.com/top/summary'
    driver.get(url)
    content=driver.page_source
    soup = BeautifulSoup(content,"lxml")
    #print (soup)
    print ('实时热搜:')
    print ('\n')
    weibo=soup.find_all('div',attrs = {'class' : 'hot_ranklist'})[0]
    weibo_content=weibo.find_all('a',attrs = {'href' :True})
    #print ('实时热搜:')
    for j in weibo_content:
        content=j.text.strip()
        print (content)

#toutiao()
print ('\n')
cnbeta()
print ('\n')
weibo()
print ('\n')
