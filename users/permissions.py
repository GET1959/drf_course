from rest_framework import permissions


class IsObjectUser(permissions.BasePermission):
    """
    Проверяет, принадлежит ли объект пользователю.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
