from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


UserAdmin.list_display += ('is_taxi',)
UserAdmin.fieldsets += (
    ('is_taxi', {
        'fields': ('is_taxi', )
    }),
)

admin.site.register(User, UserAdmin)
