from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Пользовательское разрешение - разрешать только автору."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class CustomPermissions(IsAuthenticated, IsAuthorOrReadOnly):
    """Пользовательские настройки доступа API.

    Параметры:
    - IsAuthenticated: Запрещать разрешение любому пользователю,
    не прошедшему аутентификацию.
    - IsAuthorOrReadOnly: Разрешать только автору.

    Разрешения:
    - ALL_PERMISSIONS: Объединение всех параметров в один через &.

    """

    ALL_PERMISSIONS = [IsAuthenticated & IsAuthorOrReadOnly]
