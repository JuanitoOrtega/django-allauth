from django.contrib import admin
from users.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'displayname']
    search_fields = ['user__username', 'displayname']
    list_filter = ['user__is_active', 'user__is_staff', 'user__is_superuser']
    ordering = ['user__username']

admin.site.register(Profile, ProfileAdmin)