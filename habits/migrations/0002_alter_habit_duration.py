# Generated by Django 5.0.6 on 2024-06-11 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="duration",
            field=models.PositiveIntegerField(default=20, verbose_name="Время выполнения, сек."),
        ),
    ]