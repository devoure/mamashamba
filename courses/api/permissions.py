from rest_framework.permissions import BasePermission

class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        #returns a True to grant access or false otherwise
        return obj.students.filter(id=request.user.id).exists()
