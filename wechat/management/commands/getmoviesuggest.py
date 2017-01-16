#coding=utf-8
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
import os
import time
from wechat.gamemix import *
from wechat.models import moviesuggest

class Command(BaseCommand):
    def handle(self, *args, **options):
        delete=moviesuggest.objects.all().delete()
        type=''
        movie=movie_suggest(type)
	#print tv
        for i in movie:
            insert=moviesuggest(movie_name=i['movie_name'],movie_link=i['movie_link'],movie_score=float(i['movie_score']),movie_pic=i['movie_pic'])
            insert.save()
        
        print 'over'

