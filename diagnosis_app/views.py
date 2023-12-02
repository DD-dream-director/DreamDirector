from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

# Create your views here.


def diagnosisView(request):
    '''
    診断用のビュー
    '''
    return render(request, 'diagnosis.html')
