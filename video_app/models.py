from django.db import models

# Create your models here.


class Tag(models.Model):
    '''
    タグを管理するモデル
    '''
    name = models.CharField(max_length=200, default="")


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
