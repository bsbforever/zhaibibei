__author__ = '42274'
#coding=utf8`
import requests
import selenium.webdriver
from bs4 import BeautifulSoup
import random
import time
def douyu(douyugame):
    game_list=[]
    url='HTTPs://www.douyu.com/directory/game/'+douyugame
    r = requests.get(url,verify=False)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'data-cid' : True})
    for i in live_list:
        try:
            all_game=i.find('a')
            game_count=all_game.find('span',attrs = {'class' : 'dy-num fr'}).text
	    if '.' in game_count:
		game_count=float(game_count[0:-1])*10000

            if float(game_count)>8000:
                game_link='https://www.douyu.com'+all_game['href']
                game_title=all_game['title']
                game_picture= all_game.find('img')['data-original']
                game_nickname=all_game.find('span',attrs = {'class' : 'dy-name ellipsis fl'}).text
              #  print all_game
               # print game_link
                #print game_title
                #print game_picture
                #print game_nickname
                #print game_count
                #print '\n'
                #break
    		game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                game_list.append(game_dic)

        except Exception, e:
            pass
#    print game_list
    return game_list
def panda(pandagame):
    game_list=[]
    url='http://www.panda.tv/cate/'+pandagame
    r = requests.get(url)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'class' : 'video-list-item video-no-tag video-no-cate'})
    for i in live_list:
        try:
            all_game=i.find('a')
           # print all_game
            game_count=all_game.find('span',attrs = {'class' : 'video-number'}).text
	    if '.' in game_count:
		game_count=float(game_count[0:-1])*10000
            if  float(game_count)>8000:
                game_link='http://www.panda.tv'+all_game['href']
                game_title=all_game.find('div',attrs = {'class' : 'video-title'})['title']
                game_picture= all_game.find('img',attrs = {'class' : 'video-img video-img-lazy'})['data-original']
                game_nickname=all_game.find('span',attrs = {'class' : 'video-nickname'}).text
               # print all_game
              #  print game_link
               # print game_nickname
                #print game_title
                #print game_picture
                #print game_count
                #print '\n'
    		game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                game_list.append(game_dic)
          #  break
        except Exception, e:
            pass
 #   print game_list
    return game_list
def huya(huyagame):
    game_list=[]
    url='http://www.huya.com/g/'+huyagame
    #driver = selenium.webdriver.PhantomJS()
    #driver.implicitly_wait(40)
    #driver.set_page_load_timeout(40)
    #driver.get(url)
    #time.sleep(5)
    #content=driver.page_source
    r = requests.get(url)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'class' : 'game-live-item'})
    for i in live_list:
        try:
            all_game=i
            #print all_game
            game_count=all_game.find('i',attrs = {'class' : 'js-num'}).text
	    if '.' in game_count:
		game_count=float(game_count[0:-1])*10000
            if  float(game_count)>8000:
                game_link=all_game.find('a',attrs = {'class' : 'video-info new-clickstat'})['href']
                game_title=all_game.find('a',attrs = {'class' : 'title new-clickstat'}).text.strip()
                game_picture= all_game.find('img',attrs = {'class' : 'pic'})['data-original']
                game_nickname=all_game.find('i',attrs = {'class' : 'nick'}).text
               # print all_game
              #  print game_link
               # print game_nickname
                #print game_title
                #print game_picture
                #print game_count
                #print '\n'
                game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                game_list.append(game_dic)
		#break
        except Exception, e:
            print e
        #break
    #print game_list
    return game_list

def zhanqi(zhanqigame):
    game_list=[]
    url='https://www.zhanqi.tv/'+zhanqigame
    r = requests.get(url,verify=False)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'data-room-id' : True})
    for i in live_list:
        try:
            all_game=i.find('a')
            game_count=all_game.find('span',attrs = {'class' : 'dv'}).text
            if '.' in game_count:
                game_count=float(game_count[0:-1])*10000
            if float(game_count)>8000:
                game_link='https://www.zhanqi.tv'+all_game['href']
                game_title=all_game.find('img')['alt']
                game_picture= all_game.find('img')['src']
                game_nickname=all_game.find('span',attrs = {'class' : 'anchor anchor-to-cut dv'}).text
              #  print all_game
               # print game_link
                #print game_title
                #print game_picture
                #print game_nickname
                #print game_count
                #print '\n'
                #break
                game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                game_list.append(game_dic)

        except Exception, e:
            pass
    #print game_list
    return game_list

def quanmin(quanminname):
    game_list=[]
    driver = selenium.webdriver.PhantomJS()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    url='http://www.quanmin.tv/game/'+quanminname
    driver.get(url)
    content=driver.page_source
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'class' : 'w-video animated fadeInUp'})
    for i in live_list:
        try:
            #print i
            all_game=i.find('a')
            game_count=all_game.find('span',attrs = {'class' : 'w-video_view-num'}).text
            game_count=str(game_count).strip().replace(',','')
            #print all_game
            if '.' in game_count:
                game_count=float(game_count[0:-1])*10000
            if  float(game_count)>8000:
                game_nickname=all_game.find('span',attrs = {'class' : 'w-video_nick'}).text.strip()
                game_link='http://www.quanmin.tv'+all_game['href']
                #game_title=all_game.find('img',attrs = {'class' : 'w-video_thumb'})['alt']
                #game_picture= all_game.find('img',attrs = {'class' : 'w-video_thumb'})['src']
                game_title=all_game.find('h3',attrs = {'class' : 'ellipsis w-video_title'}).text.strip()
                game_picture= all_game.find_all('img',attrs = {'alt' : ''})[1]['src']
               # print( all_game)
                #print(game_author.strip())
                #print (game_link)
                #print (game_title)
                #print (picture)
                #print (game_count)
                #print ('\n')
                #break
                game_dic={}
                game_dic['game_link']=game_link
                game_dic['game_title']=game_title
                game_dic['game_picture']=game_picture
                game_dic['game_nickname']=game_nickname
                game_dic['game_count']=game_count
                game_list.append(game_dic)
        except Exception as  e:
            #pass
            print e
    return game_list


def nowplay(type):
    movie_list=[]
    url='https://movie.douban.com/'+type
    r = requests.get(url,verify=False)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('li',attrs = {'class' : 'list-item'})
    for i in live_list:
        try:
            all_game=i
            #print (all_game)
            movie_type=all_game['data-category']
            #print (movie_type)
            if movie_type=='nowplaying':
                movie_name=all_game.find('a',attrs = {'data-psource' : 'title'}).text.strip()

                movie_link=all_game.find('a',attrs = {'data-psource' : 'title'})['href']
                #movie_actor=all_game.find('li',attrs = {'class' : 'list-item'})#['data-actors']
                movie_actor=all_game['data-actors']
                movie_director=all_game['data-director']
                movie_time=all_game['data-duration']
                movie_region=all_game['data-region']
                movie_release=all_game['data-release']
                movie_score=all_game['data-score']
                movie_pic=all_game.find('img')['src']
                movie_dic={}
                movie_dic['movie_name']=movie_name
                movie_dic['movie_link']=movie_link
                movie_dic['movie_actor']=movie_actor
                movie_dic['movie_director']=movie_director
                movie_dic['movie_time']=movie_time
                movie_dic['movie_region']=movie_region
                movie_dic['movie_release']=movie_release
                movie_dic['movie_score']=movie_score
                movie_dic['movie_pic']=movie_pic
                movie_list.append(movie_dic)
                #break
            else:
                pass
        except Exception as e:
            print (e)
    return movie_list


def tvshow(type):
    tv_list=[]
    driver = selenium.webdriver.PhantomJS()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    url='https://movie.douban.com/tv/#!type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'+type
    driver.get(url)
    time.sleep(4)
    content=driver.page_source
    #print (content)
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('a',attrs = {'class':'item'})
    #print (live_list)
    for i in live_list:
        try:
            all_game=i
            #print (i)
            tv_name=all_game.find('p').text.strip().split()[0]
            tv_link=all_game['href']
            tv_score=all_game.find('strong').text.strip()
            tv_pic=all_game.find('img')['src']
            tv_dic={}
            tv_dic['tv_name']=tv_name
            tv_dic['tv_link']=tv_link
            tv_dic['tv_score']=tv_score
            tv_dic['tv_pic']=tv_pic
            tv_list.append(tv_dic)
            #print (tv_list)
            #break
        except Exception as e:
	    print (e)
    return tv_list



def laterplay(type):
    movie_list=[]
    url='https://movie.douban.com/later/suzhou/'+type
    r = requests.get(url,verify=False)
    content=r.content
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('div',attrs = {'class' : 'item mod '})
    #print (live_list)
    for i in live_list:
        try:
            all_game=i

            #print (all_game)
            movie_preview=all_game.find('a',attrs = {'class' : 'trailer_icon'})

            movie_name=all_game.find('a',attrs = {'class' : ''}).text.strip()

            movie_link=all_game.find('a',attrs = {'class' : ''})['href']

            #movie_actor=all_game.find('li',attrs = {'class' : 'list-item'})#['data-actors']
            movie_pic=all_game.find('img',attrs = {'class' : ''})['src']
            movie_time=all_game.find_all('li',attrs = {'class' : 'dt'})[0].text.strip()
            movie_type=all_game.find_all('li',attrs = {'class' : 'dt'})[1].text.strip()
            movie_region=all_game.find_all('li',attrs = {'class' : 'dt'})[2].text.strip()
            movie_people=all_game.find_all('li',attrs = {'class' : 'dt'})[3].text.strip()
	    movie_people=float(''.join(list(movie_people)[0:-3]))
	    #print movie_people
            if movie_preview != None:
                movie_preview=all_game.find('a',attrs = {'class' : 'trailer_icon'})['href']
            else:
                movie_preview=''
            movie_dic={}
            movie_dic['movie_name']=movie_name
            movie_dic['movie_link']=movie_link
            movie_dic['movie_pic']=movie_pic
            movie_dic['movie_time']=movie_time
            movie_dic['movie_type']=movie_type
            movie_dic['movie_region']=movie_region
            movie_dic['movie_people']=movie_people
            movie_dic['movie_preview']=movie_preview
            movie_list.append(movie_dic)

            #break
        except Exception as e:
            print (e)


    live_list=soup.find_all('div',attrs = {'class' : 'item mod odd'})
    #print (live_list)
    for i in live_list:
        try:
            all_game=i

            #print (all_game)
            movie_preview=all_game.find('a',attrs = {'class' : 'trailer_icon'})

            movie_name=all_game.find('a',attrs = {'class' : ''}).text.strip()

            movie_link=all_game.find('a',attrs = {'class' : ''})['href']

            #movie_actor=all_game.find('li',attrs = {'class' : 'list-item'})#['data-actors']
            movie_pic=all_game.find('img',attrs = {'class' : ''})['src']
            movie_time=all_game.find_all('li',attrs = {'class' : 'dt'})[0].text.strip()
            movie_type=all_game.find_all('li',attrs = {'class' : 'dt'})[1].text.strip()
            movie_region=all_game.find_all('li',attrs = {'class' : 'dt'})[2].text.strip()
            movie_people=all_game.find_all('li',attrs = {'class' : 'dt'})[3].text.strip()
	    movie_people=int(''.join(list(movie_people)[0:-3]))
	    #print movie_people
            if movie_preview != None:
                movie_preview=all_game.find('a',attrs = {'class' : 'trailer_icon'})['href']
            else:
                movie_preview=''
            movie_dic={}
            movie_dic['movie_name']=movie_name
            movie_dic['movie_link']=movie_link
            movie_dic['movie_pic']=movie_pic
            movie_dic['movie_time']=movie_time
            movie_dic['movie_type']=movie_type
            movie_dic['movie_region']=movie_region
            movie_dic['movie_people']=movie_people
            movie_dic['movie_preview']=movie_preview
            movie_list.append(movie_dic)

            #break
        except Exception as e:
            print (all_game)

    return movie_list


def movie_suggest(type):
    movie_list=[]
    driver = selenium.webdriver.PhantomJS()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    url='https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'+type
    driver.get(url)
    time.sleep(4)
    content=driver.page_source
    #print (content)
    soup = BeautifulSoup(content,"lxml")
    live_list=soup.find_all('a',attrs = {'class':'item'})
    #print (live_list)
    for i in live_list:
        try:
            all_game=i
            #print (i)
            movie_name=all_game.find('p').text.strip().split()[0]
            movie_link=all_game['href']
            movie_score=all_game.find('strong').text.strip()
            movie_pic=all_game.find('img')['src']
            movie_dic={}
            movie_dic['movie_name']=movie_name
            movie_dic['movie_link']=movie_link
            movie_dic['movie_score']=movie_score
            movie_dic['movie_pic']=movie_pic
            movie_list.append(movie_dic)
            #print (tv_list)
            #break
        except Exception as e:
	    print (e)
    return movie_list





if __name__=="__main__":
    douyugame='overwatch'
    pandagame='overwatch'
    huyagame='2174'
    #douyu(douyugame)
    quanminname='overwatch'
    #panda(pandagame)
    type=''
    result=moviesuggest(type)

    for i in result:
       print i
