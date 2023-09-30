from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class User(AbstractUser):
    link = models.CharField(max_length=500)
    avatar = models.ImageField(upload_to='media/avatars/', null=True, blank=True)
