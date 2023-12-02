# coding:utf-8

from django.urls import path
from views import *

urlpatterns = [
    path('video_app/diagnosis.html'),
    path('video_app/recomment_videos.html'),
    path('video_app/other_videos.html'),
    path('video_app/other_video.html'),
]
