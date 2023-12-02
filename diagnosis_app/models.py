from django.db import models
from video_app.models import Tag
from django.contrib.auth.models import User

class User_select(Tag):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    
