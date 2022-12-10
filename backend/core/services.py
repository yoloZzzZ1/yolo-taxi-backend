from cars.models import Car


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
        raise Exception('Вы уже добавили автомобиль.')
    else:
        return Car.objects.create(**validated_data)