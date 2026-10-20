from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Allow access only to the person who owns the record."""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAdmin(BasePermission):
    """Allow access only to users whose role is 'admin'."""

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and getattr(request.user, 'role', None) == 'admin'
        )