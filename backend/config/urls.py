from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cars.views import CarModelViewSet


router = DefaultRouter()
router.register('car', CarModelViewSet, basename='car')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls))
]
