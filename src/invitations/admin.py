from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from invitations import models
from rest_framework.authtoken.models import Token


@admin.register(models.Invite)
class InviteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "reason",
        "created_at",
        "status",
    )
    list_filter = ["status"]
    search_fields = ["email", "name"]
    actions = ["approve_selected_invites", "reject_selected_invites"]

    def approve_selected_invites(self, request, queryset):
        for invite in queryset:
            user = User.objects.create(
                username=get_random_string(length=150),
                first_name=invite.name,
                email=invite.email,
                is_active=True,
            )
            Token.objects.create(user=user)

        queryset.update(status="approved")

    def reject_selected_invites(self, request, queryset):
        for invite in queryset:
            users = User.objects.filter(first_name=invite.name, email=invite.email)
            users.update(is_active=False)
            Token.objects.filter(user__in=users).delete()
        queryset.update(status="rejected")
