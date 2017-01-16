from __future__ import unicode_literals

from django.db import models

# Create your models here.

class gamelist(models.Model):
    platform=models.CharField(max_length=10)
    game_name=models.CharField(max_length=20)
    game_link=models.CharField(max_length=100)
    game_title=models.CharField(max_length=100)
    game_picture=models.CharField(max_length=300)
    game_nickname=models.CharField(max_length=100)
    game_time=models.FloatField()
    game_count=models.FloatField()
    def __unicode__(self):
        return self.game_title
    class Meta:
        app_label='wechat'


class movielist(models.Model):
    movie_name=models.CharField(max_length=50)
    movie_link=models.CharField(max_length=100)
    movie_actor=models.CharField(max_length=100)
    movie_type=models.CharField(max_length=20)
    movie_director=models.CharField(max_length=50)
    movie_time=models.CharField(max_length=20)
    movie_region=models.CharField(max_length=50)
    movie_release=models.CharField(max_length=10)
    movie_score=models.FloatField()
    movie_pic=models.CharField(max_length=100)
    def __unicode__(self):
        return self.movie_name
    class Meta:
        app_label='wechat'

class laterlist(models.Model):
    movie_name=models.CharField(max_length=50)
    movie_link=models.CharField(max_length=100)
    movie_pic=models.CharField(max_length=100)
    movie_time=models.CharField(max_length=20)
    movie_type=models.CharField(max_length=50)
    movie_region=models.CharField(max_length=20)
    movie_people=models.IntegerField()
    movie_preview=models.CharField(max_length=100)
    def __unicode__(self):
        return self.movie_name
    class Meta:
        app_label='wechat'

class tvlist(models.Model):
    tv_name=models.CharField(max_length=100)
    tv_link=models.CharField(max_length=100)
    tv_score=models.FloatField()
    tv_pic=models.CharField(max_length=100)
    def __unicode__(self):
        return self.tv_name
    class Meta:
        app_label='wechat'

class moviesuggest(models.Model):
    movie_name=models.CharField(max_length=100)
    movie_link=models.CharField(max_length=100)
    movie_score=models.FloatField()
    movie_pic=models.CharField(max_length=100)
    def __unicode__(self):
        return self.movie_name
    class Meta:
        app_label='wechat'



class oraerror(models.Model):
    error_code=models.CharField(max_length=100)
    error_message=models.TextField()
    error_cause=models.TextField()
    error_action=models.TextField()
    def __unicode__(self):
        return self.error_code
    class Meta:
        app_label='wechat'
