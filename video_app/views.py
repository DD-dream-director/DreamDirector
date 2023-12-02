from django.shortcuts import render, redirect
from .models import VideoTagName
from django.contrib.auth.models import User
from django.db import models

# Create your views here.


def diagnosisView(request):
    video_tags = VideoTagName.objects.all()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #for video_tag in video_tags:
        




def recomment_videosView(request):
    pass


def other_videosView(request):
    pass


def other_videos(request):
    pass
