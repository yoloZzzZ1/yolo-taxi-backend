from django.db import models
from users.models import User


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

    is_active = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.driver.username} -- {self.number}'
