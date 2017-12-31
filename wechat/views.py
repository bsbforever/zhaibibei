#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
import time
import urllib
import selenium.webdriver
from parse import *
from lxml import etree
from qiushibaike import joke
from movie import *
from getlyric import *
from gamemix import *
from ora import *
from tuling import *
from wechat.models import gamelist
from wechat.models import movielist
from wechat.models import tvlist
from wechat.models import laterlist
from wechat.models import moviesuggest
from wechat.models import lyrics
from wechat.models import matchlist
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpRequest
from django import template
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
WEIXIN_TOKEN='bsbforever'

@csrf_exempt
def  check(request):
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("请关注微信公众号 宅必备!")
    else:
        xml_str=request.body.decode('utf-8')
        xml = etree.fromstring(xml_str)
        messagetype = xml.find('MsgType').text
        if messagetype=='text':
            dic=parse_message(xml)
            if dic['Content'].lower()=='time':
                dic['Content']=time.ctime()
                return render_to_response('reply_message.html',dic)
            elif dic['Content'].lower()=='joke1':
	        dic['Content']=joke()
		return render_to_response('reply_message.html',dic)
            elif 'l:'in dic['Content'].lower():
		name=dic['Content'].split(':')[1]
	        #dic['Content']='sss'
		song=get_name(name)
		lyric_url1='http://www.zhaibibei.cn/lyric'+song['url']
		if lyrics.objects.filter(lyric_url=lyric_url1).exists():
		    queryset=lyrics.objects.get(lyric_url=lyric_url1)
		    dic['title']=queryset.lyric_title
		    dic['description']=queryset.lyric_title
		    dic['pic']=queryset.lyric_pic
		    dic['url']=queryset.lyric_url
		    return render_to_response('reply_lyrics.html',dic)
		else:
		    content=get_lyric('https://genius.com'+song['url'])
		    insert=lyrics(lyric_title=song['title'],lyric_url=lyric_url1,lyric_pic=song['pic'],lyric_content=content)
                    insert.save()
		    dic['Content']='歌词下载完毕，请重新输入歌名'
		    return render_to_response('reply_message.html',dic)
		time.sleep(1)
            elif 'm:' in dic['Content'].lower():
		moviename=dic['Content'].split()[-1]
		moviename=urllib.quote(moviename.encode('utf8'))
		dic['Content']=douban(moviename)
		return render_to_response('reply_message.html',dic)
            elif  '-' in dic['Content']:
		code=dic['Content'].upper()
		dic['Content']=orasearch(code)
		return render_to_response('reply_message.html',dic)
            elif 'd:' in dic['Content'].lower():
		moviename=dic['Content'].split()[-1]
		moviename=urllib.quote(moviename.encode('utf8'))
                movielink=panc(moviename)
                movielink=movielink.replace('amp;','')
		dic['Content']=movielink
		return render_to_response('reply_message.html',dic)
            elif 't:' in  dic['Content'].lower():
		dt=dic['Content'].split(':')[-1]
		try:
		    dic['Content']='输入时间对应的UNIX时间戳为:'+str(time.mktime(time.strptime(dt, '%Y%m%d%H%M%S')))
		    return render_to_response('reply_message.html',dic)
	        except Exception , e:
	            dic['Content']='请输入正确的日期格式:20160101235959'
                    return render_to_response('reply_message.html',dic)
            elif  'help' in dic['Content'].lower() or '?' in dic['Content'] or len(dic['Content'])<2:
	        dic['Content']='欢迎关注公众号，以下为具体功能:\n\n\n个人网站:http://www.zhaibibei.cn\n\n\n输入ORA-00600查询Oracle错误\n\n(支持ORA IMP EXP RMAN等错误)\n\n\n输入青椒肉丝查看做法\n\n\n输入快递+快递单号查询位置\n\n\n可以讲笑话等\n\n\n输入m:行尸走肉查看电影评分\n\n\n输入l:shape of you查看歌曲歌词\n\n\n已接入机器人，可进行自动对话'
                return render_to_response('reply_message.html',dic)
	    else:
	        #dic['Content']='欢迎关注公众号，以下为具体功能:\n\n\n个人网站:http://www.shiyue.wiki\n\n\n输入ORA-00600查询Oracle 错误\n\n\n输入Joke 查看最新笑话\n\n\n输入m行尸走肉查看电影评分\n\n\n输入d行尸走肉获取下载链接\n\n\n'
	        #dic['Content']='欢迎关注公众号，以下为具体功能:\n\n\n个人网站:http://www.shiyue.wiki\n\n\n输入ORA-00600查询Oracle错误\n\n(支持ORA IMP EXP RMAN等错误)\n\n\n输入Joke 查看最新笑话\n\n\n输入m行尸走肉查看电影评分\n\n\n'
                #return render_to_response('reply_message.html',dic)
		info=dic['Content']
		userid=dic['MsgId']
		result=tuling1(info,userid)
		if result['code']==100000:
		    dic['Content']=result['content']
		    return render_to_response('reply_message.html',dic)
		elif result['code']==200000:
		    dic['Title']=result['title']
		    dic['Description']=result['description']
		    dic['Url']=result['url']
		    dic['PicUrl']=''
		    return render_to_response('reply_link.html',dic)
		elif result['code']==302000:
		    dic['title1']=result['title1']
		    dic['description1']=result['description1']
		    dic['picurl1']=result['picurl1']
		    dic['url1']=result['url1']
		    dic['title2']=result['title2']
		    dic['description2']=result['description2']
		    dic['picurl2']=result['picurl2']
		    dic['url2']=result['url2']
		    return render_to_response('reply_news.html',dic)
		elif result['code']==308000:
		    dic['title1']=result['title1']
		    dic['description1']=result['description1']
		    dic['picurl1']=result['picurl1']
		    dic['url1']=result['url1']
		    dic['title2']=result['title2']
		    dic['description2']=result['description2']
		    dic['picurl2']=result['picurl2']
		    dic['url2']=result['url2']
		    dic['title3']=result['title3']
		    dic['description3']=result['description3']
		    dic['picurl3']=result['picurl3']
		    dic['url3']=result['url3']
		    dic['title4']=result['title4']
		    dic['description4']=result['description4']
		    dic['picurl4']=result['picurl4']
		    dic['url4']=result['url4']
		    dic['MsgType']='news'
		    return render_to_response('reply_caipu.html',dic)
                #return render_to_response('reply_message.html',dic)
        elif messagetype=='image':
            dic=parse_image(xml)
            return render_to_response('reply_image.html',dic)
        elif messagetype=='voice':
            dic=parse_voice(xml)
            return render_to_response('reply_voice.html',dic)





def index(request):
    result=gamelist.objects.values('platform').distinct().count()
    dic={'result':result}
    return render_to_response('index.html',dic)
    #return render_to_response('index.html')
    #return HttpResponse(result)

def translate(request):
    return render_to_response('translate.html')


def translateresult(request):
    result  = str(request.GET['word'])
    #return HttpResponse(name1)
    dic={'result':result}
    return render_to_response('translateresult.html',dic)

def lyric(request,title):
    #return HttpResponse(title)
    content = lyrics.objects.get(lyric_url='http://www.shiyue.wiki/lyric/'+title).lyric_content
    dic={'title':title,'content':content}
    return render_to_response('sop.html',dic)

def marathon(request):
    #return HttpResponse(title)
    content = matchlist.objects.all().order_by('match_date')
    dic={'content':content}
    return render_to_response('sop.html',dic)


def game_ow(request):
    game_time1=time.time()
    #result=gamelist.objects.filter(float(game_time)+600>=float(game_time1)).filter(game_name='overwatch').order_by('-game_count')
    result=gamelist.objects.filter(game_name='ow').order_by('-game_count')
    dic={'result':result}
    return render_to_response('ow.html',dic)

def game_sc(request):
    game_time1=time.time()
    #result=gamelist.objects.filter(float(game_time)+600>=float(game_time1)).filter(game_name='overwatch').order_by('-game_count')
    result=gamelist.objects.filter(game_name='sc').order_by('-game_count')
    dic={'result':result}
    return render_to_response('sc.html',dic)

def game_hs(request):
    gametime=float(time.time())
    result=gamelist.objects.filter(game_name='hs').order_by('-game_count')
    #result=gamelist.objects.all().filter(game_time__range=(gametime-600,game_time)).filter(game_name='hearthstone').order_by('-game_count')
    #result=gamelist.objects.filter(game_time=game_time).order_by('-game_count')
    dic={'result':result}
    return render_to_response('hs.html',dic)

def game_lol(request):
    game_time1=time.time()
    #result=gamelist.objects.filter(float(game_time)+600>=float(game_time1)).filter(game_name='lol').order_by('-game_count')
    result=gamelist.objects.filter(game_name='lol').order_by('-game_count')
    dic={'result':result}
    return render_to_response('lol.html',dic)

def game_tvgame(request):
    game_time1=time.time()
    #result=gamelist.objects.filter(float(game_time)+600>=float(game_time1)).filter(game_name='tvgame').order_by('-game_count')
    result=gamelist.objects.filter(game_name='tvgame').order_by('-game_count')
    dic={'result':result}
    return render_to_response('tvgame.html',dic)


def game_girl(request):
    #result=gamelist.objects.filter(game_time=game_time).order_by('-game_count')
    game_time1=time.time()
    #result=gamelist.objects.filter(float(game_time)+600>=float(game_time1)).filter(game_name='girl').order_by('-game_count')
    result=gamelist.objects.filter(game_name='girl').order_by('-game_count')
    dic={'result':result}
    return render_to_response('girl.html',dic)


def game_dota2(request):
    #result=gamelist.objects.filter(game_time=game_time).order_by('-game_count')
    game_time1=time.time()
    #result=gamelist.objects.filter(float(game_time)+600>=float(game_time1)).filter(game_name='girl').order_by('-game_count')
    result=gamelist.objects.filter(game_name='dota2').order_by('-game_count')
    dic={'result':result}
    return render_to_response('dota2.html',dic)

def game_badminton(request):
    #result=gamelist.objects.filter(game_time=game_time).order_by('-game_count')
    game_time1=time.time()
    #result=gamelist.objects.filter(float(game_time)+600>=float(game_time1)).filter(game_name='girl').order_by('-game_count')
    result=gamelist.objects.filter(game_name='badminton').order_by('-game_count')
    dic={'result':result}
    return render_to_response('badminton.html',dic)

def game_football(request):
    #result=gamelist.objects.filter(game_time=game_time).order_by('-game_count')
    game_time1=time.time()
    #result=gamelist.objects.filter(float(game_time)+600>=float(game_time1)).filter(game_name='girl').order_by('-game_count')
    result=gamelist.objects.filter(game_name='football').order_by('-game_count')
    dic={'result':result}
    return render_to_response('football.html',dic)

def game_hot(request):
    #result=gamelist.objects.filter(game_time=game_time).order_by('-game_count')
    game_time1=time.time()
    #result=gamelist.objects.filter(float(game_time)+600>=float(game_time1)).filter(game_name='girl').order_by('-game_count')
    result=gamelist.objects.filter(game_count__gte=100000).order_by('-game_count')
    dic={'result':result}
    return render_to_response('hot.html',dic)
def movie_nowplay(request):
    result=movielist.objects.filter(movie_type='nowplaying')
    #result=movielist.objects.filter(movie_type='nowplaying').order_by('-movie_score')
    dic={'result':result}
    return render_to_response('movie_nowplay.html',dic)


def movie_tvshow(request):
    result=tvlist.objects.all
    #result=tvlist.objects.order_by('-tv_score')
    dic={'result':result}
    return render_to_response('movie_tvshow.html',dic)

def movie_search(request):
    movie_name  = str(request.GET['name'])
    #movie_name=urllib.quote(movie_name.encode('utf8'))
    return HttpResponse('movie_name')
    #return render_to_response('movie_tvshow.html',dic)


def movie_suggest(request):
    result=moviesuggest.objects.all
    #result=tvlist.objects.order_by('-tv_score')
    dic={'result':result}
    return render_to_response('movie_suggest.html',dic)

def movie_laterplay(request):
    #result=laterlist.objects.order_by('-movie_people')
    result=laterlist.objects.all
    dic={'result':result}
    return render_to_response('movie_laterplay.html',dic)
