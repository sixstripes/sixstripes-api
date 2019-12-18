from data.models import Occupation, Politician, SexualOrientation
from django.contrib import admin, messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect
from django.urls import path

from .forms import CsvImportForm
from .translator import PoliticianDataTranslator


@admin.register(Politician)
class PoliticianAdmin(admin.ModelAdmin):
    change_list_template = "politician_changelist.html"
    list_display = (
        "name",
        "sexual_orientation",
        "country",
        "reference",
    )

    class Media:
        js = ("//code.jquery.com/jquery-3.4.1.slim.min.js", "js/admin-csv-import.js")
        css = {"all": ("css/admin-csv-import.css",)}

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("import/", self.import_csv, name="data_politician_import_csv"),
        ]
        return my_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["form"] = CsvImportForm()
        return super().changelist_view(request, extra_context=extra_context)

    def import_csv(self, request):
        if request.method != "POST":
            return HttpResponseNotAllowed(permitted_methods=["POST"])

        csv_file = request.FILES["csv_file"]
        if csv_file.content_type != "text/csv":
            self.message_user(request, "Invalid file format", level=messages.ERROR)
            return redirect("admin:data_politician_changelist")

        data_translator = PoliticianDataTranslator(csv_file)
        data_translator.parse_rows()
        data_translator.to_objects_list()

        self.message_user(request, "Your csv file has been imported")
        return redirect("admin:data_politician_changelist")


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SexualOrientation)
class SexualOrientationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
