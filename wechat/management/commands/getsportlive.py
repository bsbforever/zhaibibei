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
	

	print 'sc'
        douyuname='SC'
        pandaname='starcraft'
        huyaname='starcraft'
        douyugame=douyu(douyuname)
        for i in douyugame:
            insert=gamelist(platform='douyu',game_name='sc',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()
        
        pandagame=panda(pandaname)
        for i in pandagame:
            insert=gamelist(platform='panda',game_name='sc',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()
	try:
            huyagame=huya(huyaname)
            for i in huyagame:
                insert=gamelist(platform='huya',game_name='sc',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                insert.save()
	except Exception, e:
	    print 'huya overwatch skip....'
        zhanqiname='chns/blizzard/sc2'
        zhanqigame=zhanqi(zhanqiname)
        for i in zhanqigame:
            insert=gamelist(platform='zhanqi',game_name='sc',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()





	print 'overwatch'
        douyuname='overwatch'
        pandaname='overwatch'
        huyaname='2174'
        douyugame=douyu(douyuname)
        for i in douyugame:
            insert=gamelist(platform='douyu',game_name='overwatch',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()
        
        pandagame=panda(pandaname)
        for i in pandagame:
            insert=gamelist(platform='panda',game_name='overwatch',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()
	try:
            huyagame=huya(huyaname)
            for i in huyagame:
                insert=gamelist(platform='huya',game_name='overwatch',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                insert.save()
	except Exception, e:
	    print 'huya overwatch skip....'
        zhanqiname='chns/blizzard/watch'
        zhanqigame=zhanqi(zhanqiname)
        for i in zhanqigame:
            insert=gamelist(platform='zhanqi',game_name='overwatch',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()
        quanminname='overwatch'
	try:
            quanmingame=quanmin(quanminname)
            for i in quanmingame:
                insert=gamelist(platform='quanmin',game_name='overwatch',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                insert.save()
	except Exception, e:
	    print 'quanmin overwatch skip...'
	print 'daota2'
        douyuname='dota2'
        pandaname='dota2'
        huyaname='7'
        douyugame=douyu(douyuname)
        for i in douyugame:
            insert=gamelist(platform='douyu',game_name='dota2',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()
        
        pandagame=panda(pandaname)
        for i in pandagame:
            insert=gamelist(platform='panda',game_name='dota2',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()
	try:
            huyagame=huya(huyaname)
            for i in huyagame:
                insert=gamelist(platform='huya',game_name='dota2',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                insert.save()
	except Exception, e:
	    print 'huya overwatch skip....'
        zhanqiname='games/dota2'
        zhanqigame=zhanqi(zhanqiname)
        for i in zhanqigame:
            insert=gamelist(platform='zhanqi',game_name='dota2',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()
        quanminname='dota2'
	try:
            quanmingame=quanmin(quanminname)
            for i in quanmingame:
                insert=gamelist(platform='quanmin',game_name='dota2',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                insert.save()
	except Exception,e:
	    print 'quanmin dota2 skip...'
	print 'hearthstone'
        douyuname='how'
        pandaname='hearthstone'
        huyaname='393'
        douyugame=douyu(douyuname)
        for i in douyugame:
            insert=gamelist(platform='douyu',game_name='hearthstone',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=i['game_count'],game_time=game_time)
            insert.save()

        pandagame=panda(pandaname)
        for i in pandagame:
            insert=gamelist(platform='panda',game_name='hearthstone',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=i['game_count'],game_time=game_time)
            insert.save()
	try:
            huyagame=huya(huyaname)
            for i in huyagame:
                insert=gamelist(platform='huya',game_name='hearthstone',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                insert.save()
	except Exception, e:
	    print 'huya hs skip.....'
        zhanqiname='chns/blizzard/how'
        zhanqigame=zhanqi(zhanqiname)
        for i in zhanqigame:
            insert=gamelist(platform='zhanqi',game_name='hearthstone',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()
        quanminname='heartstone'
	try:
            quanmingame=quanmin(quanminname)
            for i in quanmingame:
                insert=gamelist(platform='quanmin',game_name='hearthstone',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                insert.save()
	except Exception, e:
	    print 'quanmin hearthstone skip..'



	print 'lol'

        douyuname='lol'
        pandaname='lol'
        huyaname='lol'
        douyugame=douyu(douyuname)
        for i in douyugame:
            insert=gamelist(platform='douyu',game_name=douyuname,game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=i['game_count'],game_time=game_time)
            insert.save()

        pandagame=panda(pandaname)
        for i in pandagame:
            insert=gamelist(platform='panda',game_name=pandaname,game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=i['game_count'],game_time=game_time)
            insert.save()
	try:
            huyagame=huya(huyaname)
            for i in huyagame:
                insert=gamelist(platform='huya',game_name='lol',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                insert.save()
	except Exception, e:
	    print 'huya lol skip.....'
        zhanqiname='games/lol'
        zhanqigame=zhanqi(zhanqiname)
        for i in zhanqigame:
            insert=gamelist(platform='zhanqi',game_name='lol',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()
        quanminname='lol'
        quanmingame=quanmin(quanminname)
        for i in quanmingame:
            insert=gamelist(platform='quanmin',game_name='lol',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()

	print 'tvgame'
        douyuname='tvgame'
        pandaname='zhuji'
        huyaname='1964'
        douyugame=douyu(douyuname)
        for i in douyugame:
            insert=gamelist(platform='douyu',game_name=douyuname,game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=i['game_count'],game_time=game_time)
            insert.save()

        pandagame=panda(pandaname)
        for i in pandagame:
            insert=gamelist(platform='panda',game_name='tvgame',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=i['game_count'],game_time=game_time)
            insert.save()
	try:
            huyagame=huya(huyaname)
            for i in huyagame:
                insert=gamelist(platform='huya',game_name='tvgame',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                insert.save()
	except Exception, e:
	    print 'huya tvgame skip......'
        zhanqiname='games/danji'
        zhanqigame=zhanqi(zhanqiname)
        for i in zhanqigame:
            insert=gamelist(platform='zhanqi',game_name='tvgame',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()
        quanminname='tvgame'
        quanmingame=quanmin(quanminname)
        for i in quanmingame:
            insert=gamelist(platform='quanmin',game_name='tvgame',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
            insert.save()



	print 'girl'
        douyuname='yz'
        pandaname='yzdr'
        huyaname='2168'
	print 'douyu'
        douyugame=douyu(douyuname)
        for i in douyugame:
            insert=gamelist(platform='douyu',game_name='girl',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=i['game_count'],game_time=game_time)
            insert.save()

	print 'panda'
        pandagame=panda(pandaname)
        for i in pandagame:
            insert=gamelist(platform='panda',game_name='girl',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=i['game_count'],game_time=game_time)
            insert.save()
	try:
            huyagame=huya(huyaname)
            for i in huyagame:
                insert=gamelist(platform='huya',game_name='girl',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                insert.save()
	except Exception, e:
	    print 'huya girl skip.....'
	print 'quanmin'
	try:
            quanminname='beauty'
            quanmingame=quanmin(quanminname)
            for i in quanmingame:
                insert=gamelist(platform='quanmin',game_name='girl',game_link=i['game_link'],game_title=i['game_title'],game_picture=i['game_picture'],game_nickname=i['game_nickname'],game_count=float(i['game_count']),game_time=game_time)
                insert.save()
	except Exception, e:
	    print 'quanmin girls skip'
        print 'over'

