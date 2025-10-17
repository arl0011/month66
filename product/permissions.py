from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsModerator(BasePermission):
    

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        
        if not user.is_staff:
            
            return True

        
        if request.method == 'POST':
            return False

        return True

    def has_object_permission(self, request, view, obj):
        
        return True
