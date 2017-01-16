#coding=utf-8
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
import os
import time
from wechat.ora import *
from wechat.models import oraerror

class Command(BaseCommand):
    def handle(self, *args, **options):
	#delete=oraerror.objects.all().delete()
	#url=geturl()
	url='https://docs.oracle.com/cd/E18283_01/server.112/e17766/crsus.htm'
	rows=oracle(url)
	for j in rows:
            insert=oraerror(error_code=j['error_code'],error_message=j['error_message'],error_cause=j['error_cause'],error_action=j['error_action'])
            insert.save()
        
        print 'over'

