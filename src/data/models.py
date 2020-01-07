from data.mixins import PersonMixin
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_countries import countries
from multiselectfield import MultiSelectField


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


class MusicalGender(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name = _("Musical Gender")
        verbose_name_plural = _("Musical Genders")
        ordering = ("slug",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class Musician(PersonMixin):
    sexual_orientation = models.ForeignKey(
        "data.SexualOrientation",
        verbose_name=_("sexual orientation"),
        related_name="musicians",
        on_delete=models.CASCADE,
    )
    musical_genders = models.ManyToManyField(
        "data.MusicalGender", verbose_name=_("musical gender"), blank=True
    )

    class Meta:
        verbose_name = _("Musician")
        verbose_name_plural = _("Musicians")

    def __str__(self):
        return self.name


class MovieDirector(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=100, unique=True)

    class Meta:
        verbose_name = _("Movie Director")
        verbose_name_plural = _("Movie Directors")

    def __str__(self):
        return self.name


class MovieGender(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=50, unique=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = _("Movie Gender")
        verbose_name_plural = _("Movie Genders")
        ordering = ("slug",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class MovieActor(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=100, unique=True)

    class Meta:
        verbose_name = _("Movie Actor")
        verbose_name_plural = _("Movie Actors")

    def __str__(self):
        return self.name


COUNTRIES_CHOICES = ((code, country) for code, country in countries.countries.items())


class Movie(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    year = models.PositiveIntegerField()
    countries = MultiSelectField(verbose_name=_("countries"), choices=COUNTRIES_CHOICES)
    reference = models.URLField(verbose_name=_("reference"), null=True, blank=True)
    genders = models.ManyToManyField(
        "data.MovieGender", related_name="movies", blank=True, verbose_name=_("movie genders")
    )
    directors = models.ManyToManyField(
        "data.MovieDirector", related_name="movies", blank=True, verbose_name=_("directors")
    )
    cast = models.ManyToManyField(
        "data.MovieActor", related_name="movies", blank=True, verbose_name=_("cast")
    )

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")

    def __str__(self):
        return self.name
