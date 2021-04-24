from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length = 256)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    text = models.TextField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
