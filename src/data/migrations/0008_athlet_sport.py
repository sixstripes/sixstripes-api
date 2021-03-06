# Generated by Django 3.0.2 on 2020-01-10 02:45

import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0007_auto_20200107_0229"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sport",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=50, unique=True, verbose_name="name")),
                ("slug", models.SlugField()),
            ],
            options={"verbose_name": "Sport", "verbose_name_plural": "Sports",},
        ),
        migrations.CreateModel(
            name="Athlet",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=256, unique=True, verbose_name="name")),
                ("country", django_countries.fields.CountryField(max_length=2, verbose_name="country")),
                ("reference", models.URLField(blank=True, null=True, verbose_name="reference")),
                (
                    "start_birth_date",
                    models.DateField(blank=True, null=True, verbose_name="start birth date"),
                ),
                ("end_birth_date", models.DateField(blank=True, null=True, verbose_name="end birth date")),
                (
                    "start_death_date",
                    models.DateField(blank=True, null=True, verbose_name="start death date"),
                ),
                ("end_death_date", models.DateField(blank=True, null=True, verbose_name="end death date")),
                (
                    "sexual_orientation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="athlets",
                        to="data.SexualOrientation",
                        verbose_name="sexual orientation",
                    ),
                ),
                (
                    "sport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="athlets",
                        to="data.Sport",
                        verbose_name="sport",
                    ),
                ),
            ],
            options={"verbose_name": "Athlet", "verbose_name_plural": "Athlets",},
        ),
    ]
