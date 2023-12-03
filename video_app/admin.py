from django.contrib import admin
from video_app.models import *


admin.site.register([Video, Tag, Comment])
