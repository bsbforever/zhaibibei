#coding=utf-8
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
import os
import time
from wechat.gamemix import *
from wechat.models import gamelist
from wechat.models import movielist

class Command(BaseCommand):
    def handle(self, *args, **options):
        delete=movielist.objects.all().delete()
        type='nowplaying/suzhou/'
        nowplaying=nowplay(type)
        for i in nowplaying:
            insert=movielist(movie_name=i['movie_name'],movie_type='nowplaying',movie_link=i['movie_link'],movie_actor=i['movie_actor'],movie_director=i['movie_director'],movie_time=i['movie_time'],movie_region=i['movie_region'],movie_release=i['movie_release'],movie_score=float(i['movie_score']),movie_pic=i['movie_pic'])
            insert.save()
        
        print 'over'

