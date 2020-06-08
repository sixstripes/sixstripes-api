import json

from data import translator
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.auth.models import User
from django.db.models import TextField
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.safestring import mark_safe
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
    list_display = ("created_at", "id", "data", "status", "reject_reason")
    formfield_overrides = {
        TextField: {"widget": JSONEditorWidget},
    }

    data_type_translators = {
        "athlet": translator.AthletDataTranslator,
        "digital-influencer": translator.DigitalInfluencerDataTranslator,
        "movie": translator.MovieDataTranslator,
        "musician": translator.MusicianDataTranslator,
        "politician": translator.PoliticianDataTranslator,
        "scientist": translator.ScientistDataTranslator,
    }

    date_type_url_names = {
        "athlet": "admin:data_athlet_change",
        "digital-influencer": "admin:data_digitalinfluencer_change",
        "movie": "admin:data_movie_change",
        "musician": "admin:data_musician_change",
        "politician": "admin:data_politician_change",
        "scientist": "admin:data_scientist_change",
    }

    actions = ["approve_suggestion"]

    def prepare_json_data(self, json_data):
        if "start_birth_date" in json_data.keys():
            birth_date = json_data.pop("start_birth_date")
            json_data["birth_date_range"] = birth_date

        if "start_death_date" in json_data.keys():
            death_date = json_data.pop("start_death_date")
            json_data["death_date_range"] = death_date

        for key, value in json_data.items():
            if type(value) == list:
                json_data[key] = ",".join(value)

    def approve_suggestion(self, request, queryset):
        for suggestion in queryset.exclude(status="approved"):
            json_data = json.loads(suggestion.data)
            data_type = json_data.pop("data_type")
            self.prepare_json_data(json_data)
            model_translator = self.data_type_translators[data_type](from_csv=False)
            cleaned_data = model_translator.clean_data(json_data)
            try:
                obj = model_translator.to_object(cleaned_data)
            except Exception as exc:
                suggestion.status = "rejected"
                suggestion.reject_reason = str(exc)
                self.message_user(request, f"Suggestion {suggestion.id} failed! {str(exc)}", messages.ERROR)
            else:
                suggestion.status = "approved"
                suggestion.reject_reason = None
                obj_url = reverse(self.date_type_url_names[data_type], args=[obj.id])
                self.message_user(
                    request,
                    mark_safe(
                        "Suggestion approved successfully! "
                        f'<a href="{obj_url}">Check integrated data here.</a>'
                    ),
                    messages.SUCCESS,
                )
            suggestion.save()
