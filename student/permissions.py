from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.methode in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class IsStaffOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.methode in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
