# admin.py
from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Post


class PostAdmin(GuardedModelAdmin):
    def has_view_permission(self, request, obj=None):
        # Check if the user has view permission at the object level
        if obj is not None:
            return request.user.has_perm("view_post", obj)
        return super().has_view_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        # Check if the user has change permission at the object level
        if obj is not None:
            return request.user.has_perm("change_post", obj)
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        # Check if the user has delete permission at the object level
        if obj is not None:
            return request.user.has_perm("delete_post", obj)
        return super().has_delete_permission(request, obj)

    def has_add_permission(self, request):
        # For adding, just use the regular model-level permission
        return super().has_add_permission(request)


admin.site.register(Post, PostAdmin)
