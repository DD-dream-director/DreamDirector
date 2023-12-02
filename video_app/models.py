from django.db import models

# Create your models here.


class VideoContent(models.Model):
    title = models.CharField(max_length=200)  # タイトル
    description = models.TextField()  # 説明
    upload_date = models.DateTimeField()  # アップロード日
    original_name = models.CharField(max_length=200)  # 管理ID
    filename = models.CharField(max_length=200, default="")  # ファイル名
    thumb_frame = models.IntegerField(default=0)  # いいねボタン
    file_type = models.CharField(max_length=100)  # 'youtube' or 'local_file'


class VideoTagName(models.Model):
    name = models.CharField(max_length=200, default="")


class VideoTagList(models.Model):
    content = models.ForeignKey(VideoContent, on_delete=models.CASCADE)
    # これはいらないかもしれない.
    tag = models.ForeignKey(VideoTagName, on_delete=models.CASCADE)
