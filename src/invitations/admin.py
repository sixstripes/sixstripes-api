from django.contrib import admin
from invitations import models


@admin.register(models.Invite)
class InviteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "reason",
        "created_at",
    )
