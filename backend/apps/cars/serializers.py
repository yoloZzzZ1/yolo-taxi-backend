from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from . import models
from core.services import check_car_add


class CarSeriliazer(serializers.ModelSerializer):

    driver = SlugRelatedField(slug_field='first_name', read_only=True)

    class Meta:
        model = models.Car
        fields = '__all__'
        read_only_fields = ['is_active']

    def create(self, validated_data):
        return check_car_add(validated_data=validated_data)

