from rest_framework.permissions import BasePermission, SAFE_METHODS

class EhDonoOuAdmin(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if request.method in SAFE_METHODS:
            # allow read if public or owner
            return getattr(obj, 'public', False) or getattr(obj, 'dono', None) == request.user

        # write: only owner
        return getattr(obj, 'dono', None) == request.user