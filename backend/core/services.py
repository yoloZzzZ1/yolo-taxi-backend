from cars.models import Car
from callings.models import Call
from rest_framework import serializers


def get_all_objects(model):
    """
    Взятие всех обьектов из бд.
    """
    return model.objects.all()


def filter_objects(model, **kwargs):
    """
    Взятие обьекта/ов из бд через фильтр.
    """
    return model.objects.filter(**kwargs)


def check_car_add(validated_data):
    """
    Проверка на добавление новой машины пользователем.
    """
    if Car.objects.filter(driver=validated_data.get("driver", None)).exists():
        raise serializers.ValidationError("Вы уже добавили автомобиль")
    else:
        return Car.objects.create(**validated_data)


def check_call_add(validated_data):
    """
    Проверка на добавление нового вызова такси пользователем.
    """
    user = validated_data.get("user", None)
    if user.is_taxi == True:
        raise serializers.ValidationError("Вы не можете вызвать такси, так как сами являетесь таксистом")
    else:
        if Call.objects.filter(user=validated_data.get("user", None), is_finished=False).exists():
            raise serializers.ValidationError("Вы уже вызвали такси, дождитесь окончания поездки")
        else:
            return Call.objects.create(**validated_data)