# coding:utf-8
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

UserModel = get_user_model()


class Tag(models.Model):
    '''
    タグを管理するモデル
    '''
    name = models.CharField(max_length=200, default="")  # タグの名前

    def __str__(self):
        '''
        Django管理画面に表示されるオブジェクト固有の名前 固有だが、primaryKeyとは異なる.
        '''
        return self.name
        pass


class Video(models.Model):
    '''
    動画ファイルや動画URL等、動画に関する情報を管理するモデル
    詳細はこのクラスによって作られるカラムを見ること
    '''
    title = models.CharField(max_length=200)  # タイトル

    description = models.TextField()  # 説明

    upload_date = models.DateTimeField()  # アップロード日

    original_name = models.CharField(max_length=200, primary_key=True)  # 管理ID

    filename = models.CharField(max_length=200, default="")  # ファイル名

    # 動画がURLなのか、uploadされたものなのかを判定するフラグを果たす
    # TrueならURL,Falseならuploadされた動画ファイル
    is_url_link = models.BooleanField()

    # url URLの長さは1000文字に制限している, NULLを許す
    url = models.URLField(max_length=1000, null=True)

    # videoのファイル,NULLを許す,settings.pyのMEDIA_ROOTをきちんと設定すること
    # 次のプルリクエストでupload_to属性をつけうること -> `kuro_dev:48063cf674d9d1c3e9e9d17fea96749e09dd7f61`より
    video = models.FileField(null=True)

    # タグを管理するカラム
    tags = models.ManyToManyField(Tag, verbose_name="タグ")

    def __str__(self):
        '''
        Django管理画面に表示されるオブジェクト固有の名前 固有だが、primaryKeyとは異なる.
        '''
        return self.title


class Comment(models.Model):
    '''
    動画に対するコメントを作成する
    '''
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        UserModel, related_name='comments_account', verbose_name='投稿者', on_delete=models.CASCADE)

    commented_to = models.ForeignKey(Video,
                                     related_name='videos',
                                     verbose_name='動画',
                                     on_delete=models.CASCADE)

    def __str__(self):
        '''
        Django管理画面に表示されるオブジェクト固有の名前
        '''
        return self.comment
