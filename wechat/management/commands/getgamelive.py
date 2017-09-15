#coding=utf-8
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
import os
import time
from wechat.gamemix import *
from wechat.models import gamelist

class Command(BaseCommand):
    def handle(self, *args, **options):
    	game_time=float(time.time())
        delete=gamelist.objects.all().delete()
	
	
	game_dic={}
	game_dic['douyu']=['sc:sc','overwatch:ow','dota2:dota2','how:hs','lol:lol','tvgame:tvgame','yz:girl']
	game_dic['panda']=['starcraft:sc','overwatch:ow','dota2:dota2','hearthstone:hs','lol:lol','zhuji:tvgame','yzdr:girl']
	game_dic['huya']=['starcraft:sc','2174:ow','7:dota2','393:hs','lol:lol','1964:tvgame','2168:girl']
	game_dic['zhanqi']=['chns/blizzard/sc2:sc','chns/blizzard/watch:ow','games/dota2:dota2','chns/blizzard/how:hs','games/lol:lol','games/danji:tvgame']
	game_dic['quanmin']=['overwatch:ow','dota2:dota2','hearthstone:hs','lol:lol','tvgame:tvgame','beauty:girl']
	
	print 'douyu'
	for game_name in game_dic['douyu']:
	    j=game_name.split(':')
	    try:
	        douyuname=douyu(j[0])
	        for i in douyuname:
		    try:
		        insert=gamelist(platform='douyu',game_name=j[1],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                        insert.save()
		    except Exception, e:
		        print 'douyu '+game_name+' insert error!'+str(e)
	    except Exception ,e:
		print 'douyu '+game_name+' get error!'+str(e)

	
	print 'panda'
	for game_name in game_dic['panda']:
	    j=game_name.split(':')
	    try:
	        pandaname=panda(j[0])
	        for i in pandaname:
		    try:
		        insert=gamelist(platform='panda',game_name=j[1],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                        insert.save()
		    except Exception, e:
		        print 'panda '+game_name+' insert error!'+str(e)
	    except Exception ,e:
		print 'panda '+game_name+' get error!'+str(e)

	print 'huya'
	for game_name in game_dic['huya']:
	    try:
		j=game_name.split(':')
	        huyaname=huya(j[0])
	        for i in huyaname:
		    try:
		        insert=gamelist(platform='huya',game_name=j[1],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                        insert.save()
		    except Exception, e:
		        print 'huya '+game_name+' insert error!'+str(e)
	    except Exception ,e:
		print 'huya '+game_name+' get error!'+str(e)
	


	print 'zhanqi'
	for game_name in game_dic['zhanqi']:
	    try:
		j=game_name.split(':')
	        zhanqiname=zhanqi(j[0])
	        for i in zhanqiname:
		    try:
		        insert=gamelist(platform='zhanqi',game_name=j[1],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                        insert.save()
		    except Exception, e:
		        print 'zhanqi '+game_name+' insert error!'+str(e)
	    except Exception ,e:
		print 'zhanqi '+game_name+' get error!'+str(e)
	
	print 'quanmin'
	for game_name in game_dic['quanmin']:
	    try:
		j=game_name.split(':')
	        quanminname=quanmin(j[0])
	        for i in quanminname:
		    try:
		        insert=gamelist(platform='quanmin',game_name=j[1],game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                        insert.save()
		    except Exception, e:
		        print 'quanmin '+game_name+' insert error!'+str(e)
	    except Exception ,e:
		print 'quanmin '+game_name+' get error!'+str(e)




	print 'badminton'
	sports='badminton'
        zhangyu1=zhangyu(sports)
        for i in zhangyu1:
            insert=gamelist(platform='zhangyu',game_name='badminton',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=i['game_count'],game_time=game_time)
            insert.save()

	print 'football'
	sports='football'
        zhangyu1=zhangyu(sports)
        for i in zhangyu1:
            insert=gamelist(platform='zhangyu',game_name='football',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=i['game_count'],game_time=game_time)
            insert.save()
	print 'over'
