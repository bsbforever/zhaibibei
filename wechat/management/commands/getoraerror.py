#coding=utf-8
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
import os
import time
from wechat.ora import *
from wechat.models import oraerror

class Command(BaseCommand):
    def handle(self, *args, **options):
	delete=oraerror.objects.all().delete()
	url=geturl()
	final_url=url[1:]
        for i in final_url:
	    print 'Now Downloding url '+i
	    time.sleep(5)
	    rows=oracle(i)
	    for j in rows:
                insert=oraerror(error_code=j['error_code'],error_message=j['error_message'],error_cause=j['error_cause'],error_action=j['error_action'])
                insert.save()
        
        print 'over'

