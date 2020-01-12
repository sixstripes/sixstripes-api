from data.mixins import PersonMixin
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_countries import countries
from django_countries.fields import CountryField


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
        return self.slug


class Occupation(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=250)
    slug = models.SlugField(max_length=250)

    class Meta:
        verbose_name = _("Occupation")
        verbose_name_plural = _("Occupations")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.slug


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
        return self.slug

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
        return self.slug

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
    countries = CountryField(verbose_name=_("country"), multiple=True)
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


class DigitalInfluencer(PersonMixin):
    sexual_orientation = models.ForeignKey(
        "data.SexualOrientation",
        verbose_name=_("sexual orientation"),
        related_name="influencers",
        on_delete=models.CASCADE,
    )
    subscribers = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("subscribers"))
    views = models.BigIntegerField(null=True, blank=True, verbose_name=_("views"))
    url = models.URLField(null=True, blank=True, verbose_name=_("url"))
    social_media_username = models.CharField(
        max_length=500, verbose_name=_("social media"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Digital Influencer")
        verbose_name_plural = _("Digital Incluencers")

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=50, unique=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = _("Sport")
        verbose_name_plural = _("Sports")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.slug


class Athlet(PersonMixin):
    sexual_orientation = models.ForeignKey(
        "data.SexualOrientation",
        verbose_name=_("sexual orientation"),
        related_name="athlets",
        on_delete=models.CASCADE,
    )
    sport = models.ForeignKey(
        "data.Sport", verbose_name=_("sport"), related_name="athlets", on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Athlet")
        verbose_name_plural = _("Athlets")

    def __str__(self):
        return self.name


class Scientist(PersonMixin):
    sexual_orientation = models.ForeignKey(
        "data.SexualOrientation",
        verbose_name=_("sexual orientation"),
        related_name="scientists",
        on_delete=models.CASCADE,
    )
    occupations = models.ManyToManyField("data.Occupation", verbose_name=_("occupations"))

    class Meta:
        verbose_name = _("Scientist")
        verbose_name_plural = _("Scientists")

    def __str__(self):
        return self.name
