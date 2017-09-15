from django.conf.urls import  url, include
from wechat import views




urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^check$',views.check, name='check'),
    url(r'^marathon$',views.marathon, name='marathon'),
    url(r'^hot$',views.game_hot, name='game_hot'),
    url(r'^ow$',views.game_ow, name='game_ow'),
    url(r'^sc$',views.game_sc, name='game_sc'),
    url(r'^hs$',views.game_hs, name='game_hs'),
    url(r'^lol$',views.game_lol, name='game_lol'),
    url(r'^dota2$',views.game_dota2, name='game_dota2'),
    url(r'^tvgame$',views.game_tvgame, name='game_tvgame'),
    url(r'^girl$',views.game_girl, name='game_girl'),
    url(r'^badminton$',views.game_badminton, name='game_badminton'),
    url(r'^football$',views.game_football, name='game_football'),
    url(r'^nowplay$',views.movie_nowplay, name='movie_nowplay'),
    url(r'^tvshow$',views.movie_tvshow, name='movie_tvshow'),
    url(r'^laterplay$',views.movie_laterplay, name='movie_laterplay'),
    url(r'^moviesuggest$',views.movie_suggest, name='movie_suggest'),
    url(r'^moviesearch$',views.movie_search, name='movie_search'),
    url(r'^lyric/(.*)$', views.lyric, name='lyric'),
]

