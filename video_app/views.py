from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from video_app.models import *


# Create your views here.

def recommend_videosView(request):
    '''
    おすすめ動画を表示するページ用のビュー
    '''
    videos = Video.objects.all()
    return render(request, 'recommend_videos.html', context={'videos': videos})


def other_videosView(request):
    '''
    おすすめ以外の動画を表示する用のビュー
    '''
    videos = get_object_or_404(Video)
    return render(request, 'other_videos.html', context={'videos': videos})


def videoView(request, video_id: int):
    '''
    動画を一つ表示し、コメントとタグを選択する用のビュー
    '''
    video = Video.objects.get(pk=video_id)
    comments = Comment.objects.filter(commented_to=video)

    return render(request, 'video.html')
