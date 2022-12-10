from django.shortcuts import render
from .serializers import CarSeriliazer
from .models import Car
from .permissions import ListCreateCar
from rest_framework import mixins, viewsets
from core.services import filter_objects


class CarModelViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin,
    mixins.ListModelMixin, viewsets.GenericViewSet
):

    """
    Возможность посмотреть свою машину.
    Возможность добавить машину, если её не существует.
    Возможность удалить машину.
    permission [is_taxi and is owner]
    """

    serializer_class = CarSeriliazer
    permission_classes = [ListCreateCar]

    def get_queryset(self):
        car = filter_objects(Car, driver=self.request.user)
        return car

    def perform_create(self, serializer):
        driver = self.request.user
        serializer.save(driver=driver)

    