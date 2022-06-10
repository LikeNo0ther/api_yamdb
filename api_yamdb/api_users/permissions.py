from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """
    Разрешение работы с пользователями только администратору.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (
                request.user.is_superuser
                or request.user.is_admin
            )


class UserOwner(permissions.BasePermission):
    """
    Разрешение пользователю работы со своим аккаунтом.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.username == request.user
