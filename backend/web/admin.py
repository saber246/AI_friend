from django.contrib import admin

from web.models.character import Character

# Register your models here.
from web.models.user import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'profile', 'create_time', 'update_time')
    list_filter = ('create_time', 'update_time')
    search_fields = ('user__username', 'user__email')
    raw_id_fields = ('user',)
    
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'create_time')
    list_filter = ('create_time',)
    search_fields = ('author__user__username', 'author__user__email')
    raw_id_fields = ('author',)
    
    