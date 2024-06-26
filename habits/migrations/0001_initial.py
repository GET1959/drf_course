# Generated by Django 5.0.6 on 2024-06-11 15:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("action", models.CharField(max_length=300, verbose_name="Действие")),
                ("place", models.CharField(max_length=300, verbose_name="Место действия")),
                ("start", models.DateTimeField(blank=True, null=True, verbose_name="Время старта действия")),
                ("is_pleasant", models.BooleanField(default=False, verbose_name="Привычка приятная")),
                ("reward", models.CharField(blank=True, max_length=300, null=True, verbose_name="Вознаграждение")),
                ("period", models.PositiveIntegerField(default=1, verbose_name="Период выполнения")),
                ("duration", models.PositiveIntegerField(default=1, verbose_name="Время выполнения, мин.")),
                ("is_public", models.BooleanField(default=False, verbose_name="Опубликована")),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Обладатель",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
