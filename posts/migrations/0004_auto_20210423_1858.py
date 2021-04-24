# Generated by Django 3.2 on 2021-04-23 18:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name = 'like',
            name = 'author',
            field = models.ForeignKey(null = True, on_delete = django.db.models.deletion.SET_NULL, related_name = 'likes',
                                      to = settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name = 'like',
            name = 'post',
            field = models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, related_name = 'likes', to = 'posts.post'),
        ),
    ]
