from rest_framework import serializers
from . import models
from rest_framework.relations import SlugRelatedField
from core.services import check_call_add
from cars.serializers import CarSeriliazer


class CallingsSerializer(serializers.ModelSerializer):

    user = SlugRelatedField(slug_field='first_name', read_only=True)
    car = CarSeriliazer(read_only=True)

    class Meta:
        model = models.Call
        fields = '__all__'
        read_only_fields = ['is_finished']

    def create(self, validated_data):
        return check_call_add(validated_data=validated_data)    