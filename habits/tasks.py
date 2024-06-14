from datetime import datetime, timedelta

import pytz
from celery import shared_task
from django.conf import settings

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def habit_reminder():
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone)
    remind_range = (now + timedelta(minutes=30), now + timedelta(minutes=31))
    habits_for_remind = Habit.objects.filter(start__range=remind_range)

    for habit in habits_for_remind:
        if habit.owner.t_chat_id:
            chat_id = habit.owner.t_chat_id
            message = f"Через 30 минут вам пора {habit.action} {habit.place}"
            send_telegram_message(chat_id, message)
            habit.start += timedelta(days=habit.period)
            habit.save()
