from django.urls import path
from diagnosis_app.views import start_diagnosis

urlpatterns = [
    path('start_diagnosis/', start_diagnosis, name='start_diagnosis'),
]
