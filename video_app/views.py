from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from video_app.models import *


# Create your views here.

def recommend_videosView(request):
    '''
    おすすめ動画を表示するページ用のビュー
    '''
    return render(request, 'recommend_videos.html')


def other_videosView(request):
    '''
    おすすめ以外の動画を表示する用のビュー
    '''
    return render(request, 'other_videos.html')


def videoView(request):
    '''
    動画を一つ表示する用のビュー
    '''
    return render(request, 'video.html')
