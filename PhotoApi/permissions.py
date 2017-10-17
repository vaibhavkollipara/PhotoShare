from rest_framework.permissions import BasePermission
from .models import Photo


class IsPhotoOwner(BasePermission):
    message = "You must be either owner of this photo or admin to delete it"

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
