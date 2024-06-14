from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class DogTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="tst@tst.ok", password="1234")
        self.habit = Habit.objects.create(
            owner=self.user,
            action="Сделать уборку",
            place="в квартире",
            start="2024-06-17 12:00:00",
            reward="отдохнуть",
            period=7,
            duration=100,
            is_public=True
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        url = reverse("habits:habit-list")
        data = {
            "action": "Послушать музыку",
            "place": "в машине",
            "start": "2024-06-18 12:00:00",
            "is_pleasant": True,
            "period": 3,
            "duration": 100,
            "is_public": True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)
        self.assertEqual(response.json(),
                         {
                             "id": self.habit.pk + 1,
                             "action": "Послушать музыку",
                             "place": "в машине",
                             "start": "2024-06-18T12:00:00Z",
                             "is_pleasant": True,
                             "reward": None,
                             "period": 3,
                             "duration": 100,
                             "is_public": True,
                             "owner": self.user.pk,
                             "related_habit": None
                         }
                         )

    def test_habit_update(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        data = {"place": "дома"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "дома")

    def test_habit_delete(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habit-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "action": "Сделать уборку",
                    "place": "в квартире",
                    "start": "2024-06-17T12:00:00Z",
                    "is_pleasant": False,
                    "reward": "отдохнуть",
                    "period": 7,
                    "duration": 100,
                    "is_public": True,
                    "owner": self.user.pk,
                    "related_habit": None
                }
            ]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
