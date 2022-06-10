from rest_framework.permissions import SAFE_METHODS, BasePermission


class SuperuserAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return (request.user.is_superuser
                    or request.user.is_admin)


class AuthorAdminModeratorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if obj.author == request.user:
            return True
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_moderator)
