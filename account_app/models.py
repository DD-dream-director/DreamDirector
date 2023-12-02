from django.db import models
from django.contrib.auth import get_user_model
from video_app.models import Tag

# Create your models here.

UserModel = get_user_model()


class Profile(models.Model):
    '''
    タグとユーザーアカウントを紐づけるモデルクラス
    '''
    user = models.OneToOneField(
        UserModel, on_delete=models.CASCADE, related_name="profile_account")
    tags = models.ManyToManyField(Tag, verbose_name="タグ")
