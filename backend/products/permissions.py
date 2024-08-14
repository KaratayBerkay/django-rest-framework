from rest_framework.permissions import DjangoModelPermissions


class IsStaffEditorPermissions(DjangoModelPermissions):
    all_permissions = None

    def has_permission(self, request, view):
        return view.perm_name in request.user.get_all_permissions()

    # def has_object_permission(self, request, view, obj):
    #     return view.perm_name in request.user.get_all_permissions()
