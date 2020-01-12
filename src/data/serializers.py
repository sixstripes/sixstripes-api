from data import models
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Occupation
        fields = ("name", "slug")


class PoliticianSerializer(CountryFieldMixin, serializers.ModelSerializer):
    occupations = OccupationSerializer(many=True)

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
            "occupations",
        )
