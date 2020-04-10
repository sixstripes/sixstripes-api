import json

from invitations import models
from rest_framework import serializers


class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invite
        fields = ("name", "email", "reason")


class DataSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataSuggestion
        fields = ("data",)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["data"] = json.loads(instance.data)
        return response

    def to_internal_value(self, data):
        sent_data = data.get("data")

        if not sent_data:
            raise serializers.ValidationError({"data": "This field is required."})

        json_string = json.dumps(sent_data)
        data["data"] = json_string
        return super().to_internal_value(data)
