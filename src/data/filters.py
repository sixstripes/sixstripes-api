from data import models
from django_filters import rest_framework as filters


class PoliticianFilterSet(filters.FilterSet):
    sexual_orientation = filters.CharFilter(field_name="sexual_orientation__slug")

    class Meta:
        model = models.Politician
        fields = {
            "name": ["exact", "icontains", "istartswith"],
            "country": ["exact"],
            "start_birth_date": ["exact", "gte", "gt", "lte", "lt"],
            "end_birth_date": ["exact", "gte", "gt", "lte", "lt"],
            "start_death_date": ["exact", "gte", "gt", "lte", "lt"],
            "end_death_date": ["exact", "gte", "gt", "lte", "lt"],
            "sexual_orientation": ["exact"],
            "occupations__slug": ["in"],
        }


class AthletsFilterSet(filters.FilterSet):
    sexual_orientation = filters.CharFilter(field_name="sexual_orientation__slug")
    sport = filters.CharFilter(field_name="sport__slug")

    class Meta:
        model = models.Athlet
        fields = {
            "name": ["exact", "icontains", "istartswith"],
            "country": ["exact"],
            "start_birth_date": ["exact", "gte", "gt", "lte", "lt"],
            "end_birth_date": ["exact", "gte", "gt", "lte", "lt"],
            "start_death_date": ["exact", "gte", "gt", "lte", "lt"],
            "end_death_date": ["exact", "gte", "gt", "lte", "lt"],
            "sexual_orientation": ["exact"],
            "sport": ["exact"],
        }


class MusicianFilterSet(filters.FilterSet):
    sexual_orientation = filters.CharFilter(field_name="sexual_orientation__slug")

    class Meta:
        model = models.Musician
        fields = {
            "name": ["exact", "icontains", "istartswith"],
            "country": ["exact"],
            "start_birth_date": ["exact", "gte", "gt", "lte", "lt"],
            "end_birth_date": ["exact", "gte", "gt", "lte", "lt"],
            "start_death_date": ["exact", "gte", "gt", "lte", "lt"],
            "end_death_date": ["exact", "gte", "gt", "lte", "lt"],
            "sexual_orientation": ["exact"],
            "musical_genders__slug": ["in"],
        }


class MovieFilterSet(filters.FilterSet):
    class Meta:
        model = models.Movie
        fields = {
            "name": ["exact", "icontains", "istartswith"],
            "countries": ["in"],
            "year": ["exact", "gte", "gt", "lte", "lt"],
            "genders__slug": ["in"],
        }


class DigitalInfluencerFilterSet(filters.FilterSet):
    sexual_orientation = filters.CharFilter(field_name="sexual_orientation__slug")

    class Meta:
        model = models.DigitalInfluencer
        fields = {
            "name": ["exact", "icontains", "istartswith"],
            "country": ["exact"],
            "start_birth_date": ["exact", "gte", "gt", "lte", "lt"],
            "end_birth_date": ["exact", "gte", "gt", "lte", "lt"],
            "start_death_date": ["exact", "gte", "gt", "lte", "lt"],
            "end_death_date": ["exact", "gte", "gt", "lte", "lt"],
            "sexual_orientation": ["exact"],
            "main_social_medias__slug": ["in"],
        }


class ScientistFilterSet(filters.FilterSet):
    sexual_orientation = filters.CharFilter(field_name="sexual_orientation__slug")

    class Meta:
        model = models.Scientist
        fields = {
            "name": ["exact", "icontains", "istartswith"],
            "country": ["exact"],
            "start_birth_date": ["exact", "gte", "gt", "lte", "lt"],
            "end_birth_date": ["exact", "gte", "gt", "lte", "lt"],
            "start_death_date": ["exact", "gte", "gt", "lte", "lt"],
            "end_death_date": ["exact", "gte", "gt", "lte", "lt"],
            "sexual_orientation": ["exact"],
            "occupations__slug": ["in"],
        }
