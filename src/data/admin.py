from data import models
from django.contrib import admin

from .mixins import ImportCSVAdminMixin
from .translator import (
    AthletDataTranslator,
    DigitalInfluencerDataTranslator,
    MovieDataTranslator,
    MusicianDataTranslator,
    PoliticianDataTranslator,
    ScientistDataTranslator,
)


@admin.register(models.Politician)
class PoliticianAdmin(ImportCSVAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "sexual_orientation",
        "country",
        "reference",
    )
    translator_class = PoliticianDataTranslator
    import_csv_url_name = "data_politician_import_csv"
    import_csv_redirect_url_name = "admin:data_politician_changelist"


@admin.register(models.Occupation)
class OccupationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.SexualOrientation)
class SexualOrientationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.MusicalGenre)
class MusicalGenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Musician)
class MusicianAdmin(ImportCSVAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "sexual_orientation",
        "country",
        "reference",
    )
    translator_class = MusicianDataTranslator
    import_csv_url_name = "data_musician_import_csv"
    import_csv_redirect_url_name = "admin:data_musician_changelist"


@admin.register(models.MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Movie)
class MovieAdmin(ImportCSVAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "year",
        "reference",
    )
    translator_class = MovieDataTranslator
    import_csv_url_name = "data_movie_import_csv"
    import_csv_redirect_url_name = "admin:data_movie_changelist"


@admin.register(models.DigitalInfluencer)
class DigitalInfluencerAdmin(ImportCSVAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "sexual_orientation",
        "country",
        "reference",
    )
    translator_class = DigitalInfluencerDataTranslator
    import_csv_url_name = "data_digitalinfluencer_import_csv"
    import_csv_redirect_url_name = "admin:data_digitalinfluencer_changelist"


@admin.register(models.Athlet)
class AthletAdmin(ImportCSVAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "sexual_orientation",
        "country",
        "reference",
    )
    translator_class = AthletDataTranslator
    import_csv_url_name = "data_athlet_import_csv"
    import_csv_redirect_url_name = "admin:data_athlet_changelist"


@admin.register(models.Scientist)
class ScientistAdmin(ImportCSVAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "sexual_orientation",
        "country",
        "reference",
    )
    translator_class = ScientistDataTranslator
    import_csv_url_name = "data_scientist_import_csv"
    import_csv_redirect_url_name = "admin:data_scientist_changelist"
