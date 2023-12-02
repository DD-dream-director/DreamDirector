from django.shortcuts import render
from django.db import models
from .models import User_select, User


def diagnosisView(request):
    if request.method == 'POST':
        user_name = request.post.get('user_name')
        video_tag = request.post.get('video_tag')

        diagnosis = User_select(user_name=user_name, video_tag=video_tag)
        diagnosis.save()

        return render(request, 'diagnosis.html')
    
    return render(request, 'diagnosis.html')
        


        
