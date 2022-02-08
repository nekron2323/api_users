from rest_framework import permissions

class IsAdmin(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user.is_admin