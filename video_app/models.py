from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class VideoContent(models.Model):
    title = models.CharField(max_length=200)  # タイトル

    description = models.TextField()  # 説明

    upload_date = models.DateTimeField()  # アップロード日

    original_name = models.CharField(max_length=200, primary_key=True)  # 管理ID

    filename = models.CharField(max_length=200, default="")  # ファイル名

    thumb_frame = models.IntegerField(default=0)  # いいねボタン

    content_type = models.CharField(
        max_length=100)  # 'youtube' or 'local_file'

    # youtube url
    url_path = models.URLField(
        max_length=1000, null=True
    )

    # local video
    video = models.FileField(
        null=True
    )


class VideoTag(models.Model):
    '''
    '''
    name = models.CharField(max_length=200, default="")


class UserRefTag(models.Model):
    '''
    '''
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    tag = models.ForeignKey(VideoTag, on_delete=models.PROTECT)


class VideoTagList(models.Model):
    content = models.ForeignKey(VideoContent, on_delete=models.CASCADE)
    # これはいらないかもしれない.
    tag = models.ForeignKey(VideoTag, on_delete=models.CASCADE)
