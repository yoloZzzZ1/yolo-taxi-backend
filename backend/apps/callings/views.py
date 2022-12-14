from rest_framework import mixins, viewsets
from .serializers import CallingsSerializer, CallingsSerializerForDriver
from core.services import filter_objects
from cars.models import Car
from .models import Call
from random import randint
from . permissions import IsTaxiOrReadOnly
from rest_framework import serializers


class CallModelViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin,
    mixins.ListModelMixin, viewsets.GenericViewSet
):

    """
    Возможность клиенту создать вызов, если его не существует.
    Возможность водителю изменить статус вызова на "завершённый".
    Возможность посмотреть активный вызов.
    permissions = [IsTaxiOrReadOnly]
    serializer = [Optional]
    """

    permission_classes = [IsTaxiOrReadOnly]

    def get_serializer_class(self):

        if self.request.user.is_taxi:
            return CallingsSerializerForDriver
        else:
            return CallingsSerializer

    def get_queryset(self):

        if self.request.user.is_taxi == True:
            return filter_objects(Call, is_finished=False, car__driver=self.request.user.id)
        else:
            return filter_objects(Call, is_finished=False, user=self.request.user)

    def perform_create(self, serializer):
        free_drivers = filter_objects(Car, is_active=False).count()

        if free_drivers < 1:
            raise serializers.ValidationError('Свободных машин сейчас нет, попробуйте позже.')
        else:
            random_driver = filter_objects(Car, is_active=False)[randint(0, free_drivers - 1)]
            user = self.request.user
            serializer.save(user=user, car=random_driver)
            random_driver.is_active = True
            random_driver.save()
    
    def perform_update(self, serializer):
        car = Car.objects.get(driver=self.request.user)
        car.is_active = False
        car.save()
        return super().perform_update(serializer)



