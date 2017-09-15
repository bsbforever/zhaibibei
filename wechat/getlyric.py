#coding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import MySQLdb
import json
def get_name(name):
    song={}
    url='https://genius.com/api/search/multi?q='+name
    r=requests.get(url)
    #print type(r.content)
    result=r.content
    result=json.loads(result)
    result=result['response']['sections'][0]['hits'][0]['result']
    title=result['full_title']
    pic=result['header_image_thumbnail_url']
    url=result['path']
    song['title']=title
    song['pic']=pic
    song['url']=url
    return song




def get_lyric(url):
    final_lyric=''
    r=requests.get(url)

    content=r.content
    #print (content)
    soup = BeautifulSoup(content,"lxml")
    #match=soup.find_all('section')
    lyric1=soup.find_all('div',attrs = {'class' : 'song_body-lyrics'})[0].text
    #match=soup.find_all('div',attrs = {'class' : 'lyrics'})
    #print str(lyric)
    lyric=lyric1.split('\n')
    for i in lyric:
	if i =='More on Genius':
	    break
	#elif i!='' or '\\2014' in i:
	#elif  '\\2014' in i:
	 #   i.replace('\\2014',' ')
	    #return i
	  #  final_lyric=final_lyric+'\n'+i

	else:
	    final_lyric=final_lyric+'\n'+i
	    #pass
    return final_lyric

if __name__=="__main__":
    result=get_name('call me maybe')

    print result

