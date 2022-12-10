from django.shortcuts import render
from .serializers import CarSeriliazer
from .models import Car
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
    permission [later]
    """

    serializer_class = CarSeriliazer

    def get_queryset(self):
        car = filter_objects(Car, driver=self.request.user)
        return car

    def perform_create(self, serializer):
        driver = self.request.user
        serializer.save(driver=driver)

    