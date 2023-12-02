from django.urls import path
from .views import diagnosisView

app_name = 'dianosis_app'

urlpatterns = [
    path('', diagnosisView.as_view(), name='diagnosis')
]
