from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):

    driver = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'driver'
    )

    color = models.CharField(
        max_length = 48
    )

    brand = models.CharField(
        max_length = 48
    )

    number = models.CharField(
        max_length = 6,
        unique=True
    )

    def __str__(self):
        return f'{self.driver.username} -- {self.number}'
