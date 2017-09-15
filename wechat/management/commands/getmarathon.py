#coding=utf-8
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
import os
import time
from wechat.marathon import *
from wechat.models import matchlist

class Command(BaseCommand):
    def handle(self, *args, **options):
        delete=matchlist.objects.all().delete()
        month=['01','02','03','04','05','06','07','08','09','10','11','12']
	for i in month:
            match_list=get_matchlist(i)
            for i in match_list:
                insert=matchlist(match_name=i['match_name'],match_address=i['match_address'],match_date=i['match_date'],match_website=i['match_website'],match_count=i['match_count'],match_detail=i['match_detail'])
                insert.save()
       	    time.sleep(5) 

