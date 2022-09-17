from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class CheckAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # if request.method not in permissions.SAFE_METHODS:
        if request.method in ('DELETE', 'PUT', 'POST', 'PATCH'):
            return obj.author == request.user
        return True
