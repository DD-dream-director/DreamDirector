from django.db import models
#from video_app.models import 
from django.contrib.auth.models import User

class User_select(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    video_tag = models.CharField(max_length=100)
