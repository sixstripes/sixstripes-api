from data.mixins import PersonMixin
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class SexualOrientation(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=50)
    initials = models.CharField(verbose_name=_("initials"), max_length=5)
    slug = models.SlugField()

    class Meta:
        verbose_name = _("Sexual Orientation")
        verbose_name_plural = _("Sexual Orientations")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.initials = self.name[0].upper()

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Occupation(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name = _("Occupation")
        verbose_name_plural = _("Occupations")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Politician(PersonMixin):
    sexual_orientation = models.ForeignKey(
        "data.SexualOrientation",
        verbose_name=_("sexual orientation"),
        related_name="politicians",
        on_delete=models.CASCADE,
    )
    occupations = models.ManyToManyField("data.Occupation", verbose_name=_("occupations"))

    class Meta:
        verbose_name = _("Politician")
        verbose_name_plural = _("Politicians")

    def __str__(self):
        return self.name
