import pandas as pd
from django.db import transaction
from django.utils.text import slugify
from django_countries import countries
from django_countries.fields import Country

from .models import (
    Athlet,
    DigitalInfluencer,
    Movie,
    MovieActor,
    MovieDirector,
    MovieGender,
    MusicalGender,
    Musician,
    Occupation,
    Politician,
    Scientist,
    SexualOrientation,
    Sport,
)
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

    @transaction.atomic
    def to_object(self, data):
        obj = self.model_class()
        for field, colum in self.field_relation.items():
            setattr(obj, field, data[field])
        obj.save()
        return obj

    def prepare_country(self, value):
        if not value:
            return Country(code="")

        return Country(countries.by_name(value))

    def prepare_date_range(self, value):
        if value is None:
            return None

        if not value.strip():
            return None

        parser = DatetimeParser(value)
        return parser.date_range()

    def prepare_birth_date_range(self, value):
        return self.prepare_date_range(value)

    def prepare_death_date_range(self, value):
        return self.prepare_date_range(value)

    @transaction.atomic
    def prepare_sexual_orientation(self, value):
        orientation = SexualOrientation.objects.get_or_create(slug=slugify(value), defaults={"name": value})
        return orientation[0]


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

    @transaction.atomic
    def prepare_occupation(self, value):
        if value is None:
            return None

        occupation = Occupation.objects.get_or_create(slug=slugify(value), defaults={"name": value})
        return occupation[0]

    def prepare_primary_occupation(self, value):
        return self.prepare_occupation(value)

    def prepare_secondary_occupation(self, value):
        return self.prepare_occupation(value)

    @transaction.atomic
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


class MusicianDataTranslator(CsvDataTranslator):

    field_relation = {
        "name": "Name",
        "sexual_orientation": "LGBTQ",
        "musical_genders": "Gender",
        "country": "Country",
        "reference": "Reference",
        "birth_date_range": "Birth",
        "death_date_range": "Death",
    }

    @transaction.atomic
    def prepare_musical_genders(self, value):
        if not value:
            return None

        genders_data = value.split(",")
        genders = [
            MusicalGender.objects.get_or_create(slug=slugify(gender_name), defaults={"name": gender_name})[0]
            for gender_name in genders_data
            if gender_name
        ]
        return genders

    @transaction.atomic
    def to_object(self, data):
        obj = Musician.objects.update_or_create(
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

        if data["musical_genders"]:
            for gender in data["musical_genders"]:
                obj.musical_genders.add(gender)

        return obj


class MovieDataTranslator(CsvDataTranslator):

    field_relation = {
        "name": "Name",
        "year": "Year",
        "directors": "Director",
        "countries": "Country",
        "reference": "Reference",
        "genders": "Gender",
        "cast": "Cast",
    }

    def __init__(self, csv_data):
        super().__init__(csv_data)
        self.actor_names = set()
        self.director_names = set()
        self.gender_names = set()

        self.populate_names()
        self.genders = self.save_genders()
        self.actors = self.save_actors()
        self.directors = self.save_directors()

    def populate_names(self):
        for idx, row in self.dataframe.iterrows():
            self.actor_names.update(self.extended_string_to_list(row["Cast"]))
            self.director_names.update(self.extended_string_to_list(row["Director"]))
            self.gender_names.update(self.extended_string_to_list(row["Gender"]))

    def save_genders(self):
        genders = [MovieGender(name=name, slug=slugify(name)) for name in self.gender_names if name]
        MovieGender.objects.all().delete()
        return MovieGender.objects.bulk_create(genders)

    def save_actors(self):
        actors = [MovieActor(name=name) for name in self.actor_names if name]
        MovieActor.objects.all().delete()
        return MovieActor.objects.bulk_create(actors)

    def save_directors(self):
        directors = [MovieDirector(name=name) for name in self.director_names if name]
        MovieDirector.objects.all().delete()
        return MovieDirector.objects.bulk_create(directors)

    @transaction.atomic
    def prepare_genders(self, value):
        if not value:
            return None

        gender_names = self.extended_string_to_list(value)

        return MovieGender.objects.in_bulk(gender_names, field_name="name").values()

    def extended_string_to_list(self, extended_string):
        if not extended_string:
            return []

        extended_string = ",".join(extended_string.split(" and "))
        return [value.strip().title() for value in extended_string.split(",")]

    @transaction.atomic
    def prepare_directors(self, value):
        if not value:
            return None

        director_names = self.extended_string_to_list(value)
        return MovieDirector.objects.in_bulk(director_names, field_name="name").values()

    @transaction.atomic
    def prepare_cast(self, value):
        if not value:
            return None

        actor_names = self.extended_string_to_list(value)
        return MovieActor.objects.in_bulk(actor_names, field_name="name").values()

    def prepare_countries(self, value):
        if not value:
            return None

        countries_list = value.split(",")

        return [Country(countries.by_name(country.strip())) for country in countries_list]

    @transaction.atomic
    def to_object(self, data):
        obj = Movie.objects.update_or_create(
            name=data["name"],
            defaults={"year": data["year"], "reference": data["reference"], "countries": data["countries"]},
        )[0]

        if data["genders"]:
            obj.genders.add(*data["genders"])

        if data["directors"]:
            obj.directors.add(*data["directors"])

        if data["cast"]:
            obj.cast.add(*data["cast"])

        return obj


class DigitalInfluencerDataTranslator(CsvDataTranslator):

    field_relation = {
        "name": "Channel",
        "sexual_orientation": "LGBTQ",
        "country": "Country",
        "reference": "Reference",
        "birth_date_range": "Birth",
        "subscribers": "Subscribers",
        "views": "Views",
        "url": "Channel Link",
        "social_media_username": "Social Media",
    }

    def prepare_subscribers(self, value):
        cleaned = value.replace(".", "")
        cleaned = cleaned.replace(",", "")
        return int(cleaned)

    def prepare_views(self, value):
        cleaned = value.replace(".", "")
        cleaned = cleaned.replace(",", "")
        return int(cleaned)

    @transaction.atomic
    def to_object(self, data):
        obj_data = {
            "sexual_orientation": data["sexual_orientation"],
            "reference": data["reference"],
            "country": data["country"],
            "subscribers": data["subscribers"],
            "views": data["views"],
            "url": data["url"],
            "social_media_username": data["social_media_username"],
        }

        if data["birth_date_range"]:
            obj_data["start_birth_date"] = data["birth_date_range"][0]
            obj_data["end_birth_date"] = data["birth_date_range"][1]

        obj = DigitalInfluencer.objects.update_or_create(name=data["name"], defaults=obj_data,)[0]

        return obj


class AthletDataTranslator(CsvDataTranslator):

    field_relation = {
        "name": "Name",
        "sexual_orientation": "LGBTQ",
        "country": "Country",
        "reference": "Reference",
        "birth_date_range": "Nascimento",
        "death_date_range": "Morte",
        "sport": "Esporte",
    }

    def __init__(self, csv_data):
        super().__init__(csv_data)
        self.sports = set()

        self.populate_sports()
        self.save_sports()

    def populate_sports(self):
        for idx, row in self.dataframe.iterrows():
            self.sports.update([row["Esporte"].strip()])

    def save_sports(self):
        sports = [Sport(name=name) for name in self.sports if name]
        Sport.objects.all().delete()
        return Sport.objects.bulk_create(sports)

    def prepare_sport(self, value):
        if not value:
            return None

        sports = Sport.objects.in_bulk([value], field_name="name")
        return sports[value]

    @transaction.atomic
    def to_object(self, data):
        obj_data = {
            "sexual_orientation": data["sexual_orientation"],
            "reference": data["reference"],
            "country": data["country"],
            "sport": data["sport"],
        }

        if data["birth_date_range"]:
            obj_data["start_birth_date"] = data["birth_date_range"][0]
            obj_data["end_birth_date"] = data["birth_date_range"][1]

        if data["death_date_range"]:
            obj_data["start_death_date"] = data["death_date_range"][0]
            obj_data["end_death_date"] = data["death_date_range"][1]

        obj = Athlet.objects.update_or_create(name=data["name"], defaults=obj_data,)[0]

        return obj


class ScientistDataTranslator(CsvDataTranslator):

    field_relation = {
        "name": "Name",
        "sexual_orientation": "LGBTQ",
        "primary_occupation": "Occupation",
        "secondary_occupation": "Occupation 2",
        "third_occupation": "Occupation 3",
        "country": "Country",
        "reference": "Reference",
        "birth_date_range": "Birth",
        "death_date_range": "Death",
    }

    @transaction.atomic
    def prepare_occupation(self, value):
        if value is None:
            return None

        occupation = Occupation.objects.get_or_create(slug=slugify(value), defaults={"name": value.title()})
        return occupation[0]

    def prepare_primary_occupation(self, value):
        return self.prepare_occupation(value)

    def prepare_secondary_occupation(self, value):
        return self.prepare_occupation(value)

    def prepare_third_occupation(self, value):
        return self.prepare_occupation(value)

    @transaction.atomic
    def to_object(self, data):
        obj_data = {
            "sexual_orientation": data["sexual_orientation"],
            "reference": data["reference"],
            "country": data["country"],
        }

        if data["birth_date_range"]:
            obj_data["start_birth_date"] = data["birth_date_range"][0]
            obj_data["end_birth_date"] = data["birth_date_range"][1]

        if data["death_date_range"]:
            obj_data["start_death_date"] = data["death_date_range"][0]
            obj_data["end_death_date"] = data["death_date_range"][1]

        obj = Scientist.objects.update_or_create(name=data["name"], defaults=obj_data,)[0]

        if data["primary_occupation"]:
            obj.occupations.add(data["primary_occupation"])

        if data["secondary_occupation"]:
            obj.occupations.add(data["secondary_occupation"])

        if data["third_occupation"]:
            obj.occupations.add(data["third_occupation"])

        return obj
