from rest_framework.serializers import ValidationError


class RelateRewardValidator:
    """Исключает одновременный выбор связанной привычки и указания вознаграждения."""
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        related_habit = value.get(self.field_1)
        reward = value.get(self.field_2)
        if related_habit and reward:
            raise ValidationError("Совместное использование связанной привычки и вознаграждения недопустимо.")


class DurationValidator:
    """Ограничивает время выполнения до 120 секунд."""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = value.get(self.field)
        if duration:
            if duration > 120:
                raise ValidationError("Время выполнения не должно превышать 120 секунд.")


class RelatedHabitValidator:
    """Допускает в связанную привычку только приятную."""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get(self.field)
        if related_habit:
            if not related_habit.is_pleasant:
                raise ValidationError("Связанная привычка должна быть приятной.")


class PleasantValidator:
    """Не допускает связанную привычку или вознаграждение для приятной привычки."""
    def __init__(self, field_1, field_2, field_3):
        self.field_1 = field_1
        self.field_2 = field_2
        self.field_3 = field_3

    def __call__(self, value):
        is_pleasant = value.get(self.field_1)
        related_habit = value.get(self.field_2)
        reward = value.get(self.field_3)
        if is_pleasant and (related_habit or reward):
            raise ValidationError("Для приятной привычки не допускается связанная привычка или вознаграждение.")


class PeriodValidator:
    """Ограничение максимального периода выполнения привычки"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        period = value.get(self.field)
        if period:
            if period > 7:
                raise ValidationError("Периодичность выполнения не должна превышать 7 дней.")
