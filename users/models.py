from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='media/avatars/', null=True, blank=True)
