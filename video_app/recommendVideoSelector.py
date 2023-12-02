# coding:utf-8
from video_app.models import *
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def select(user_id: int):
    """おすすめを提示するためのアルゴリズム

    Args:
        user_id (int): auth_userテーブルのidカラム(<- プライマリーキー)
    """
    pass


if __name__ == "__main__":
    select()
