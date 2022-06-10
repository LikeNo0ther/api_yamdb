from datetime import datetime
from django.core.exceptions import ValidationError


def year_validator(value):
    if value > datetime.now().year:
        raise ValidationError(
            'Нельзя добавить произведение которое ещё не вышло')
    if value < 0:
        raise ValidationError(
            'Поле не может иметь отрицательное значение')
