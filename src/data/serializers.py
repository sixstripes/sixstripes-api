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


class MovieGenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieGender
        fields = ("name", "slug")


class MovieSerializer(CountryFieldMixin, serializers.ModelSerializer):
    genders = serializers.StringRelatedField(many=True)
    cast = serializers.StringRelatedField(many=True)
    directors = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Movie
        fields = (
            "id",
            "name",
            "year",
            "countries",
            "reference",
            "genders",
            "directors",
            "cast",
        )


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialMedia
        fields = ("name", "slug")


class DigitalInfluencerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    sexual_orientation = serializers.StringRelatedField()
    main_social_medias = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.DigitalInfluencer
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
            "subscribers",
            "views",
            "url",
            "social_media_username",
            "main_social_medias",
        )


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sport
        fields = ("name", "slug")


class AthletSerializer(CountryFieldMixin, serializers.ModelSerializer):
    sexual_orientation = serializers.StringRelatedField()
    sport = serializers.StringRelatedField()

    class Meta:
        model = models.Athlet
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
            "sport",
        )


class ScientistSerializer(CountryFieldMixin, serializers.ModelSerializer):
    occupations = serializers.StringRelatedField(many=True)
    sexual_orientation = serializers.StringRelatedField()

    class Meta:
        model = models.Scientist
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
