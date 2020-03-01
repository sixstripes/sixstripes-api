from invitations import models
from rest_framework import serializers


class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invite
        fields = ("name", "email", "reason")
