#coding=utf-8
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
import os
import time
from wechat.gamemix import *
from wechat.models import tvlist

class Command(BaseCommand):
    def handle(self, *args, **options):
        delete=tvlist.objects.all().delete()
        type=''
        tv=tvshow(type)
	#print tv
        for i in tv:
            insert=tvlist(tv_name=i['tv_name'],tv_link=i['tv_link'],tv_score=float(i['tv_score']),tv_pic=i['tv_pic'])
            insert.save()
        
        print 'over'

