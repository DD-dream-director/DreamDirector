# coding:utf-8
from video_app.models import *
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from video_app.models import *


UserModel = get_user_model()


def select(user_id: int):
    """おすすめを提示するためのアルゴリズム

    Args:
        user_id (int): auth_userテーブルのidカラム(<- プライマリーキー)
    """
    # recommend_videos = Video.objects.filter(tags=)


if __name__ == "__main__":
    select()
