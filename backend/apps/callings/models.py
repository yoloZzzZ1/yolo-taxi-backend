from django.db import models
from cars.models import Car
from users.models import User


class Call(models.Model):

    car = models.ForeignKey(
        Car,
        on_delete = models.CASCADE,
    )

    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'client'
    )

    adress = models.CharField(
        max_length = 256
    )

    is_finished = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.car.number} -- {self.user.username}'
    

