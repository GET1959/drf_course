# Generated by Django 5.0.6 on 2024-06-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="t_chat_id",
            field=models.PositiveIntegerField(default=0, verbose_name="chat_id"),
        ),
    ]
