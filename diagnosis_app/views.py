from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from video_app.models import Tag

UserModel = get_user_model()


def diagnosisView(request):
    '''
    サインアップ直後の診断用
    '''
    tags = Tag.objects.all()

    return render(request, 'diagnosis.html', context={'tags': tags})
