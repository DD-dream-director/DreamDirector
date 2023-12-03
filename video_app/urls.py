# coding:utf-8
from django.urls import path
from video_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recommend_videos/',recommend_videosView,name="recommend_videos"), # おすすめ動画を表示するルーティング
    path('other_videos/',other_videosView,name="other_videos"), # おすすめ以外の動画を表示するルーティング
    path('video/<int:original_name>/',videoView,name="video"), # 動画を一つ表示するページ
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #メディアフォルダーの有効化