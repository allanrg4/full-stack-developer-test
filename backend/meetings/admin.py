from django.contrib import admin

from meetings.models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass
