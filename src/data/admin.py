from data.models import MusicalGender, Musician, Occupation, Politician, SexualOrientation
from django.contrib import admin

from .mixins import ImportCSVAdminMixin
from .translator import MusicianDataTranslator, PoliticianDataTranslator


@admin.register(Politician)
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


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SexualOrientation)
class SexualOrientationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(MusicalGender)
class MusicalGenderAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Musician)
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
