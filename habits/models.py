from django.conf import settings
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name="Обладатель")
    action = models.CharField(max_length=300, verbose_name="Действие")
    place = models.CharField(max_length=300, verbose_name="Место действия")
    start = models.DateTimeField(**NULLABLE, verbose_name="Время старта действия")
    is_pleasant = models.BooleanField(default=False, verbose_name="Привычка приятная")
    related_habit = models.ForeignKey("self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Связанная привычка")
    reward = models.CharField(max_length=300, **NULLABLE, verbose_name="Вознаграждение")
    period = models.PositiveIntegerField(default=1, verbose_name="Период выполнения")
    duration = models.PositiveIntegerField(default=20, verbose_name="Время выполнения, сек.")
    is_public = models.BooleanField(default=False, verbose_name="Опубликована")

    def __str__(self):
        return f"Привычка {self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ("id",)
