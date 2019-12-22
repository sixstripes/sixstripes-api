from django.contrib import messages
from django.db import models
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect
from django.urls import path
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from .forms import CsvImportForm


class PersonMixin(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=256)
    country = CountryField(verbose_name=_("country"))
    reference = models.URLField(verbose_name=_("reference"), null=True, blank=True)
    start_birth_date = models.DateField(verbose_name=_("start birth date"), null=True, blank=True)
    end_birth_date = models.DateField(verbose_name=_("end birth date"), null=True, blank=True)
    start_death_date = models.DateField(verbose_name=_("start death date"), null=True, blank=True)
    end_death_date = models.DateField(verbose_name=_("end death date"), null=True, blank=True)

    class Meta:
        abstract = True


class ImportCSVAdminMixin:
    class Media:
        js = ("//code.jquery.com/jquery-3.4.1.slim.min.js", "js/admin-csv-import.js")
        css = {"all": ("css/admin-csv-import.css",)}

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("import/", self.import_csv, name=self.import_csv_url_name),
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
            return redirect(self.import_csv_redirect_url_name)

        data_translator = self.translator_class(csv_file)
        data_translator.parse_rows()
        data_translator.to_objects_list()

        self.message_user(request, "Your csv file has been imported")
        return redirect(self.import_csv_redirect_url_name)
