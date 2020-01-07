from data import models
from django.contrib import admin

from .mixins import ImportCSVAdminMixin
from .translator import (
    DigitalInfluencerDataTranslator,
    MovieDataTranslator,
    MusicianDataTranslator,
    PoliticianDataTranslator,
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


@admin.register(models.MusicalGender)
class MusicalGenderAdmin(admin.ModelAdmin):
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


@admin.register(models.MovieGender)
class MovieGenderAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Movie)
class MovieAdmin(ImportCSVAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "year",
        "countries",
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
