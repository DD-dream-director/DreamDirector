# coding:utf-8
from django.urls import path
from video_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD
    path('recommend_videos/',recommend_videosView,name="recommend_videos"), # おすすめ動画を表示するルーティング
    path('other_videos/',other_videosView,name="other_videos"), # おすすめ以外の動画を表示するルーティング
    path('video/<int:original_name>/',videoView,name="video"), # 動画を一つ表示するページ
=======
    path('recommend_videos/', recommend_videosView,
         name="recommend_videos"),  # おすすめ動画を表示するルーティング
    path('other_videos/', other_videosView,
         name="other_videos"),  # おすすめ以外の動画を表示するルーティング
    path('video/<int:video_id>', videoView, name="video"),  # 動画を一つ表示するページ
    path('post_video/', postView, name='post_video'),  # 動画を投稿するページ
>>>>>>> b2427b1bc811df64a979fba0adba8ceb333004f5
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #メディアフォルダーの有効化