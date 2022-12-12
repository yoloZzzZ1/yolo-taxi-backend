from rest_framework import permissions

class IsTaxiOrReadOnly(permissions.BasePermission):
    message = 'У вас недостаточно прав.'

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return request.user.first_name == obj.car.driver.first_name