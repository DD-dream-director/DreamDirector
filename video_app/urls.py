# coding:utf-8

from django.urls import path
from views import *

urlpatterns = [
    path('diagnosis/',diagnosisView,name="diagnosis"), # タグがいっぱいあるやつ
    path('recommend_videos/',recommend_videosView,name="recommend_videos"), # おすすめ動画を表示するルーティング
    path('other_videos/',other_videosView,name="other_videos"), # おすすめ以外の動画を表示するルーティング
    path('other_video/',other_videoView,name="other_video"), # 
]
