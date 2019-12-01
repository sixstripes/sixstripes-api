import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Occupation",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                ("slug", models.SlugField()),
            ],
            options={"verbose_name": "Occupation", "verbose_name_plural": "Occupations"},
        ),
        migrations.CreateModel(
            name="SexualOrientation",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                ("initials", models.CharField(max_length=5, verbose_name="initials")),
                ("slug", models.SlugField()),
            ],
            options={"verbose_name": "Sexual Orientation", "verbose_name_plural": "Sexual Orientations"},
        ),
        migrations.CreateModel(
            name="Politician",
            fields=[
                (
                    "id",
                    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
                ),
                ("name", models.CharField(max_length=256, verbose_name="name")),
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
                ("occupation", models.ManyToManyField(to="data.Occupation", verbose_name="occupation")),
                (
                    "sexual_orientation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="politicians",
                        to="data.SexualOrientation",
                        verbose_name="sexual orientation",
                    ),
                ),
            ],
            options={"verbose_name": "Politician", "verbose_name_plural": "Politicians"},
        ),
    ]
