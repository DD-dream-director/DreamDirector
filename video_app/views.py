from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from video_app.models import *


# Create your views here.

def recommend_videosView(request):
    '''
    おすすめ動画を表示するページ用のビュー
    '''
    videos = Video.objects.all()
    return render(request, 'video_app/recommend_videos.html', context={'videos': videos})


def other_videosView(request):
    '''
    おすすめ以外の動画を表示する用のビュー
    '''
    videos = get_object_or_404(Video)
    return render(request, '/video_app/other_videos.html', context={'videos': videos})


<<<<<<< HEAD
def videoView(request, original_name):
    '''
    動画を一つ表示する用のビュー(松山)
    '''
    video = get_object_or_404(Video, pk=original_name)
    name = Video.title
    tags = Video.tags
    return render(request, 'video.html', {'video': video, 'name': name, 'tags': tags})
=======
def videoView(request, video_id: int):
    '''
    動画を一つ表示し、コメントとタグを選択する用のビュー
    '''
    video = Video.objects.get(pk=video_id)
    comments = Comment.objects.filter(commented_to=video)

    return render(request, 'video_app/video.html')


def postView(request):
    '''
    動画投稿用のビュー
    '''
    return render(request, 'video_app/post_video.html')
>>>>>>> b2427b1bc811df64a979fba0adba8ceb333004f5
