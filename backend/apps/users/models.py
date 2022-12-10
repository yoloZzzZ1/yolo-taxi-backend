import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_taxi = models.BooleanField(default=False)