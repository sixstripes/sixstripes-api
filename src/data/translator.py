import pandas as pd
from django.utils.text import slugify
from django_countries import countries
from django_countries.fields import Country

from .models import Occupation, Politician, SexualOrientation
from .utils import DatetimeParser


class CsvDataTranslator:
    field_relation = {}

    def __init__(self, csv_data):
        self.data = []
        self.dataframe = pd.read_csv(csv_data).replace({pd.np.nan: None})

    def default_prepare_field(self, value):
        return value

    def parse_rows(self):
        for idx, row in self.dataframe.iterrows():
            self.data.append(self.prepare_data(row))

    def prepare_data(self, csv_row):
        data = {}
        for field, column in self.field_relation.items():
            prepare_field = getattr(self, f"prepare_{field}", None)
            if not prepare_field or not callable(prepare_field):
                data[field] = self.default_prepare_field(csv_row[column])
                continue

            data[field] = prepare_field(csv_row[column])
        return data

    def to_objects_list(self):
        return [self.to_object(data_dict) for data_dict in self.data]

    def to_object(self, data):
        obj = self.model_class()
        for field, colum in self.field_relation.items():
            setattr(obj, field, data[field])
        obj.save()
        return obj


class PoliticianDataTranslator(CsvDataTranslator):

    field_relation = {
        "name": "Name",
        "sexual_orientation": "LGBTQ",
        "primary_occupation": "Occupation",
        "secondary_occupation": "Occupation 2",
        "country": "Country",
        "reference": "Reference",
        "birth_date_range": "Birth",
        "death_date_range": "Death",
    }

    def prepare_sexual_orientation(self, value):
        orientation = SexualOrientation.objects.get_or_create(slug=slugify(value), defaults={"name": value})
        return orientation[0]

    def prepare_country(self, value):
        return Country(countries.by_name(value))

    def prepare_date_range(self, value):
        if value is None:
            return None

        parser = DatetimeParser(value)
        return parser.date_range()

    def prepare_birth_date_range(self, value):
        return self.prepare_date_range(value)

    def prepare_death_date_range(self, value):
        return self.prepare_date_range(value)

    def prepare_occupation(self, value):
        if value is None:
            return None

        occupation = Occupation.objects.get_or_create(slug=slugify(value), defaults={"name": value})
        return occupation[0]

    def prepare_primary_occupation(self, value):
        return self.prepare_occupation(value)

    def prepare_secondary_occupation(self, value):
        return self.prepare_occupation(value)

    def to_object(self, data):
        obj = Politician.objects.update_or_create(
            name=data["name"],
            defaults={
                "sexual_orientation": data["sexual_orientation"],
                "reference": data["reference"],
                "country": data["country"],
            },
        )[0]

        if data["birth_date_range"]:
            obj.start_birth_date = data["birth_date_range"][0]
            obj.end_birth_date = data["birth_date_range"][1]

        if data["death_date_range"]:
            obj.start_death_date = data["death_date_range"][0]
            obj.end_death_date = data["death_date_range"][1]

        obj.save()

        if data["primary_occupation"]:
            obj.occupations.add(data["primary_occupation"])

        if data["secondary_occupation"]:
            obj.occupations.add(data["secondary_occupation"])

        return obj
