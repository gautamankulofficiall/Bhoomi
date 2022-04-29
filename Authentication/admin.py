from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_filter = ('is_staff', 'is_verified', 'is_active', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    ordering = ('-created_at',)