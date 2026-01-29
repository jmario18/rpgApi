from rest_framework.permissions import BasePermission, SAFE_METHODS

class EhDonoOuAdmin(BasePermission):
    # tem que ser has_permission ou has_object_permission
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if request.method in SAFE_METHODS:
            return True
        
        return obj.dono == request.user