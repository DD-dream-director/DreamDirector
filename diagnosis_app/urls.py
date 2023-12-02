from django.urls import path
from diagnosis_app.views import diagnosisView

urlpatterns = [
    path('diagnosis/', diagnosisView, name='diagnosis'),
]
