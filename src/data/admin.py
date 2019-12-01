from data.models import Occupation, Politician, SexualOrientation
from django.contrib import admin


@admin.register(Politician)
class PoliticianAdmin(admin.ModelAdmin):
    pass


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SexualOrientation)
class SexualOrientationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
