from django_filters.rest_framework.backends import DjangoFilterBackend
from drf_yasg.inspectors import CoreAPICompatInspector, NotHandled
from drf_yasg.openapi import Parameter


class BaseFieldInspector(CoreAPICompatInspector):
    custom_filters = {}

    def get_filter_parameters(self, filter_backend):
        if isinstance(filter_backend, DjangoFilterBackend):
            result = []
            filters = {}
            for param in super().get_filter_parameters(filter_backend):
                splitted_param = param.name.split("__")

                if len(splitted_param) == 1:
                    result.append(param)
                    continue

                available_filters = filters.get(splitted_param[0], [])
                available_filters.append(f"`{splitted_param[-1]}`")
                filters[splitted_param[0]] = available_filters

            for param in result:
                available_filters = filters.get(param.name, None)
                if available_filters:
                    param.description += "Available filters: " + ", ".join(available_filters)

            return result + self.get_custom_filters()

        return NotHandled

    def get_custom_filters(self):
        parameters = []
        for field, field_data in self.custom_filters.items():
            param = Parameter(
                name=field,
                in_=field_data["in"],
                description=field_data["description"],
                type=field_data["type"],
                required=field_data["required"],
            )
            parameters.append(param)

        return parameters


class PoliticianScientistFieldInspector(BaseFieldInspector):
    custom_filters = {
        "occupations": {
            "in": "query",
            "description": "Should be used with `__slug` suffix. Available filters: `in`",
            "type": "string",
            "required": False,
        }
    }


class MusicianFieldInspector(BaseFieldInspector):
    custom_filters = {
        "musical_genres": {
            "in": "query",
            "description": "Should be used with `__slug` suffix. Available filters: `in`",
            "type": "string",
            "required": False,
        }
    }


class MovieFieldInspector(BaseFieldInspector):
    custom_filters = {
        "genres": {
            "in": "query",
            "description": "Should be used with `__slug` suffix. Available filters: `in`",
            "type": "string",
            "required": False,
        },
        "countries": {
            "in": "query",
            "description": "Available filters: `in`",
            "type": "string",
            "required": False,
        },
    }


class DigitalInfluencerFieldInspector(BaseFieldInspector):
    custom_filters = {
        "main_social_media": {
            "in": "query",
            "description": "Should be used with `__slug` suffix. Available filters: `in`",
            "type": "string",
            "required": False,
        }
    }
