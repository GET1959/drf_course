from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitViewSet(ModelViewSet):
    """Viewset for Habit."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = CustomPagination
    permission_classes = [IsOwner]

    def get_queryset(self):
        if self.action == "list":
            filter_query = Q(owner=self.request.user) | Q(is_public=True)
            return Habit.objects.filter(filter_query)
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
