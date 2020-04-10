from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import TextField
from django.utils.crypto import get_random_string
from django_json_widget.widgets import JSONEditorWidget
from invitations import models
from rest_framework.authtoken.models import Token
from templated_email import send_templated_mail


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
        for invite in queryset.exclude(status="approved"):
            user = User.objects.create(
                username=get_random_string(length=150),
                first_name=invite.name,
                email=invite.email,
                is_active=True,
            )
            token = Token.objects.create(user=user)
            send_templated_mail(
                template_name="invite_approved",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[invite.email],
                context={"invite": invite, "token": token},
            )

        queryset.update(status="approved")

    def reject_selected_invites(self, request, queryset):
        for invite in queryset.exclude(status="rejected"):
            users = User.objects.filter(first_name=invite.name, email=invite.email)
            users.update(is_active=False)
            Token.objects.filter(user__in=users).delete()
        queryset.update(status="rejected")


@admin.register(models.DataSuggestion)
class DataSuggestionAdmin(admin.ModelAdmin):
    list_display = ("created_at", "data")
    formfield_overrides = {
        TextField: {
            "widget": JSONEditorWidget(
                options={
                    "mode": "tree",
                    "sortObjectKeys": True,
                    "modes": [],
                    "navigationBar": False,
                    "mainMenuBar": False,
                    "statusBar": False,
                }
            )
        },
    }
