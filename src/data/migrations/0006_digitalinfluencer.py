# Generated by Django 3.0.2 on 2020-01-07 02:16

import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0005_auto_20200106_2249"),
    ]

    operations = [
        migrations.CreateModel(
            name="DigitalInfluencer",
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
                    "subscribers",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="subscribers"),
                ),
                ("views", models.BigIntegerField(blank=True, null=True, verbose_name="views")),
                ("url", models.URLField(blank=True, null=True, verbose_name="url")),
                ("social_media_username", models.CharField(max_length=500, verbose_name="social media")),
                (
                    "sexual_orientation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="influencers",
                        to="data.SexualOrientation",
                        verbose_name="sexual orientation",
                    ),
                ),
            ],
            options={"verbose_name": "Digital Influencer", "verbose_name_plural": "Digital Incluencers",},
        ),
    ]
