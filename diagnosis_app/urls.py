from django.urls import path
from video_app.views import *

urlpatterns = [
    path('diagnosis/', diagnosisView, name='diagnosis'),
]
