from django.conf import settings
from django.db import models


class Like(models.Model):
    post = models.ForeignKey('post', on_delete = models.CASCADE, related_name = 'likes')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True, related_name = 'likes')
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        unique_together = (
            'post',
            'author',
        )
