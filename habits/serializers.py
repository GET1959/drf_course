from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (DurationValidator, PeriodValidator,
                               PleasantValidator, RelatedHabitValidator,
                               RelateRewardValidator)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RelateRewardValidator(field_1="related_habit", field_2="reward"),
            DurationValidator(field="duration"),
            RelatedHabitValidator(field="related_habit"),
            PleasantValidator(field_1="is_pleasant", field_2="related_habit", field_3="reward"),
            PeriodValidator(field="period")
        ]
