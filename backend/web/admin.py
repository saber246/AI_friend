from django.contrib import admin

# Register your models here.
from web.models.user import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'profile', 'create_time', 'update_time')
    list_filter = ('create_time', 'update_time')
    search_fields = ('user__username', 'user__email')
    raw_id_fields = ('user',)