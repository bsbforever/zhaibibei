from django.contrib import admin
from wechat.models import gamelist
from wechat.models import movielist
from wechat.models import lyrics
from wechat.models import matchlist
from wechat.models import laterlist
from wechat.models import tvlist
from wechat.models import moviesuggest
from wechat.models import oraerror
# Register your models here.
admin.site.register(gamelist)
admin.site.register(movielist)
admin.site.register(matchlist)
admin.site.register(laterlist)
admin.site.register(tvlist)
admin.site.register(moviesuggest)
admin.site.register(oraerror)
admin.site.register(lyrics)

