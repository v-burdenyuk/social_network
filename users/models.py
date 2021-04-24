from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    last_activity = models.DateTimeField(auto_now = True)
