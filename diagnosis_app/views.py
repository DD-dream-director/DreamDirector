from django.shortcuts import render
from django.db import models
from .models import User_select, User
from django.contrib.auth.decorators import login_required


def diagnosisView(request):
    if request.method == 'POST':
        #form = フォームを記入
        if form.is_valid():
            selected_tag = form.save(commit=False)
            selected_tag.user = request.user
            selected_tag.save()

    else:
        #form =  フォームの名前
        return render(request, 'index')
    
    return render(request, 'index')
        


        
