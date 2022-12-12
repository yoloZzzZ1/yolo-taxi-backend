from rest_framework import mixins, viewsets
from .serializers import CallingsSerializer
from core.services import filter_objects
from cars.models import Car
from .models import Call
from random import randint
from . permissions import IsTaxiOrReadOnly


class CallModelViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin,
    mixins.ListModelMixin, viewsets.GenericViewSet
):

    """
    Возможность клиенту создать вызов, если его не существует.
    Возможность водителю изменить статус вызова на "звершённый".
    Возможность посмотреть активный вызов.
    permissions = [IsTaxiOrReadOnly]
    """

    serializer_class = CallingsSerializer
    permission_classes = [IsTaxiOrReadOnly]

    def get_queryset(self):
        return filter_objects(Call, is_finished=False, user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        free_drivers = filter_objects(Car, is_active=False).count()
        random_driver = filter_objects(Car, is_active=False)[randint(0, free_drivers - 1)]
        serializer.save(user=user, car=random_driver)
        random_driver.is_active = True
        random_driver.save()

    def perform_update(self, serializer):
        is_finished = True
        serializer.save(is_finished=is_finished)