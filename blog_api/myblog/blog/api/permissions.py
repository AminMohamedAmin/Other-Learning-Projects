# each user can update to his owen posts only

from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = "you din't have permission"
    def has_object_permission(self, request, view, obj):
        return obj.user==request.user