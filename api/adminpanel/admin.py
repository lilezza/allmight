from django.contrib import admin
from django.contrib.auth.models import User

class CustomAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_superuser  # فقط سوپر یوزر!

admin.site = CustomAdminSite()
admin.site.register(User)
