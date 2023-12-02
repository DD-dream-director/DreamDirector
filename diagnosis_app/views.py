from .forms import SelectedTagForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from video_app.models import Tag


UserModel = get_user_model()


def diagnosisView(request):
    '''
    サインアップ直後の診断用
    '''
    if request.method == 'POST':
        form = SelectedTagForm(request.POST)
        if form.is_valid():
            selected_tag = form.save(commit=False)
            selected_tag.user = request.user
            selected_tag.save()

    else:
        form =  SelectedTagForm()
        return render(request, 'diagnosis.html')
 
 
    tags = Tag.objects.all()

    return render(request, 'diagnosis.html', context={'tags': tags})
