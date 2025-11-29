from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    message = "Only Admin can reach this page."

    def has_permission(self, request, view):
        return request.user.is_admin and request.user.is_authenticated
    
class IsStudent(permissions.BasePermission):
    message = "Permission Denied."

    def has_permission(self, request, view):
        return (request.user.is_student and request.user.is_authenticated) or request.user.is_admin

class IsCommAgent(permissions.BasePermission):
    message = "Only Community Agents can reach this page"

    def has_permission(self, request, view):
        return request.user.is_comm_agent and request.user.is_authenticated
    
class IsStudentOrCommAgent(permissions.BasePermission):
    message = "You must be either a student or a comm agent."

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and ((user.is_student or user.is_comm_agent) or user.is_admin)