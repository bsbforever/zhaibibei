#coding=utf-8
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
import os
import time
from wechat.gamemix import *
from wechat.models import laterlist

class Command(BaseCommand):
    def handle(self, *args, **options):
        delete=laterlist.objects.all().delete()
        type=''
        laterplaying=laterplay(type)
        for i in laterplaying:
            insert=laterlist(movie_name=i['movie_name'],movie_link=i['movie_link'],movie_pic=i['movie_pic'],movie_time=i['movie_time'],movie_type=i['movie_type'],movie_region=i['movie_region'],movie_people=i['movie_people'],movie_preview=i['movie_preview'])
            insert.save()
        
        print 'over'

