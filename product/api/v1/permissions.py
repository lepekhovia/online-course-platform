from rest_framework.permissions import BasePermission, SAFE_METHODS
from courses.models import Purchase


def make_payment(request):
    # TODO
    pass


class IsStudentOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        pass

    def has_object_permission(self, request, view, obj):
        pass


class ReadOnlyOrIsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in SAFE_METHODS


class OnlyStaffCanChangedBalance(BasePermission):
    safe_methods = ['GET', 'HEAD', 'OPTIONS', 'PATCH']

    def has_permission(self, request, view):
        if request.user.is_staff and request.method in self.safe_methods:
            return True
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff and request.method in self.safe_methods:
            return True
        if request.user.is_superuser:
            return True
        return False
