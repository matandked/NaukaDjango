# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post

# ten model będzie widoczny w panelu admina
admin.site.register(Post)
