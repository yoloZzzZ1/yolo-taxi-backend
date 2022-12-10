from rest_framework import permissions


class ListCreateCar(permissions.BasePermission):
    message = 'У вас недостаточно прав.'

    def has_permission(self, request, view):
        return (
            request.user.is_taxi
        )

    def has_object_permission(self, request, view, obj):
        return obj.driver == request.user