from data import models
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Occupation
        fields = ("name", "slug")


class SexualOrientationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SexualOrientation
        fields = ("name", "slug")


class PoliticianSerializer(CountryFieldMixin, serializers.ModelSerializer):
    occupations = serializers.StringRelatedField(many=True)
    sexual_orientation = serializers.StringRelatedField()

    class Meta:
        model = models.Politician
        fields = (
            "id",
            "name",
            "country",
            "reference",
            "start_birth_date",
            "end_birth_date",
            "start_death_date",
            "end_death_date",
            "sexual_orientation",
            "occupations",
        )


class MusicalGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MusicalGender
        fields = ("name", "slug")


class MusicianSerializer(CountryFieldMixin, serializers.ModelSerializer):
    musical_genders = serializers.StringRelatedField(many=True)
    sexual_orientation = serializers.StringRelatedField()

    class Meta:
        model = models.Politician
        fields = (
            "id",
            "name",
            "country",
            "reference",
            "start_birth_date",
            "end_birth_date",
            "start_death_date",
            "end_death_date",
            "sexual_orientation",
            "musical_genders",
        )
