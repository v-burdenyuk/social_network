# Generated by Django 3.2 on 2021-04-23 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name = 'post',
            name = 'author',
            field = models.ForeignKey(default = 1, on_delete = django.db.models.deletion.CASCADE, to = 'auth.user'),
            preserve_default = False,
        ),
    ]
