from django.contrib import admin

from .models.like import Like
from .models.post import Post

admin.site.register(Post)
admin.site.register(Like)
