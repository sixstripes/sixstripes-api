# Generated by Django 3.0.1 on 2019-12-30 20:07

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0003_auto_20191222_2333"),
    ]

    operations = [
        migrations.CreateModel(
            name="MovieActor",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="name")),
            ],
            options={"verbose_name": "Movie Actor", "verbose_name_plural": "Movie Actors",},
        ),
        migrations.CreateModel(
            name="MovieDirector",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=100, unique=True, verbose_name="name")),
            ],
            options={"verbose_name": "Movie Director", "verbose_name_plural": "Movie Directors",},
        ),
        migrations.CreateModel(
            name="MovieGender",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=50, unique=True, verbose_name="name")),
                ("slug", models.SlugField()),
            ],
            options={
                "verbose_name": "Movie Gender",
                "verbose_name_plural": "Movie Genders",
                "ordering": ("slug",),
            },
        ),
        migrations.AlterModelOptions(
            name="musicalgender",
            options={
                "ordering": ("slug",),
                "verbose_name": "Musical Gender",
                "verbose_name_plural": "Musical Genders",
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("year", models.PositiveIntegerField()),
                ("country", django_countries.fields.CountryField(max_length=2, verbose_name="country")),
                ("reference", models.URLField(blank=True, null=True, verbose_name="reference")),
                (
                    "cast",
                    models.ManyToManyField(
                        blank=True, related_name="movies", to="data.MovieActor", verbose_name="cast"
                    ),
                ),
                (
                    "directors",
                    models.ManyToManyField(
                        blank=True, related_name="movies", to="data.MovieDirector", verbose_name="directors"
                    ),
                ),
                (
                    "genders",
                    models.ManyToManyField(
                        blank=True, related_name="movies", to="data.MovieGender", verbose_name="movie genders"
                    ),
                ),
            ],
            options={"verbose_name": "Movie", "verbose_name_plural": "Movies",},
        ),
    ]