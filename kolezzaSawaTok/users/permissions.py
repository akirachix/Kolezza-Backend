from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class IsAuthenticatedAndHasPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.has_perm(
            "your_permission_name"
        )


class HasSpeechTherapistPermissions(BasePermission):
    """
    Custom permission to only allow authenticated users with a specific permission.
    """

    def has_permission(self, request, view):
        edit_methods = ["POST", "GET", "PATCH", "DELETE"]

        if request.method in edit_methods:
            if request.user_permissions in [
                "can_view_patient_info",
                "can_edit_modules",
                "can_register_children",
                "can_view_progress_reports",
            ]:
                return True
            else:
                return False

        return request.user.has_perm("app_label.permission_name")


class HasSuperUserPermissions(BasePermission):
    """
    Custom permission to only allow superusers with full access.
    """

    def has_permission(self, request, view):
        edit_methods = ["POST", "GET", "PATCH", "DELETE"]

        if request.method in edit_methods:
            if request.user_permissions in [
                "Full CRUD access (Create, Read, Update, Delete) to all resources",
                "Ability to manage user roles and permissions",
                "Access to view and edit patient information",
                "Access to view and edit progress reports"
                "Ability to register, edit, and delete children profiles"
                "Access to view and edit all modules"
                "Access to administrative actions (e.g., database management, backups)"
                "Ability to view and access audit logs",
            ]:
                return True
            else:
                return False
