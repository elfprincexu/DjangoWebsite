from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadyOnly(BasePermission):
    message = "You must be the owner of the object"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
