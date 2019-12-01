from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class PersonMixin(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=256)
    country = CountryField(verbose_name=_("country"))
    reference = models.URLField(verbose_name=_("reference"), null=True, blank=True)
    start_birth_date = models.DateField(verbose_name=_("start birth date"), null=True)
    end_birth_date = models.DateField(verbose_name=_("end birth date"), null=True)
    start_death_date = models.DateField(verbose_name=_("start death date"), null=True)
    end_death_date = models.DateField(verbose_name=_("end death date"), null=True)

    class Meta:
        abstract = True
