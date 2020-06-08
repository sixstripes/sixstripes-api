import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0013_auto_20200113_0048"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="countries",
            field=django_countries.fields.CountryField(
                blank=True, max_length=746, multiple=True, verbose_name="country"
            ),
        ),
        migrations.AlterField(
            model_name="movie", name="year", field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
