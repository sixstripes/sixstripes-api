from data import filters, models, serializers, swagger
from django.utils.decorators import method_decorator
from django_countries import countries
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, permissions, response, views, viewsets


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        filter_inspectors=[swagger.PoliticianScientistFieldInspector], operation_summary="list politicians"
    ),
)
@method_decorator(name="retrieve", decorator=swagger_auto_schema(operation_summary="detail politician"))
class PoliticianViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Politician.objects.all()
    serializer_class = serializers.PoliticianSerializer
    filterset_class = filters.PoliticianFilterSet


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        filter_inspectors=[swagger.MusicianFieldInspector], operation_summary="list musicians"
    ),
)
@method_decorator(name="retrieve", decorator=swagger_auto_schema(operation_summary="detail musician"))
class MusicianViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Musician.objects.all()
    serializer_class = serializers.MusicianSerializer
    filterset_class = filters.MusicianFilterSet


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        filter_inspectors=[swagger.MovieFieldInspector], operation_summary="list movies"
    ),
)
@method_decorator(name="retrieve", decorator=swagger_auto_schema(operation_summary="detail movie"))
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    filterset_class = filters.MovieFilterSet


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        filter_inspectors=[swagger.DigitalInfluencerFieldInspector],
        operation_summary="list digital influencers",
    ),
)
@method_decorator(
    name="retrieve", decorator=swagger_auto_schema(operation_summary="detail digital influencer")
)
class DigitalInfluencerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DigitalInfluencer.objects.all()
    serializer_class = serializers.DigitalInfluencerSerializer
    filterset_class = filters.DigitalInfluencerFilterSet


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        filter_inspectors=[swagger.BaseFieldInspector], operation_summary="list athletes"
    ),
)
@method_decorator(name="retrieve", decorator=swagger_auto_schema(operation_summary="detail athlet"))
class AthletViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Athlet.objects.all()
    serializer_class = serializers.AthletSerializer
    filterset_class = filters.AthletsFilterSet


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        filter_inspectors=[swagger.PoliticianScientistFieldInspector], operation_summary="list scientists"
    ),
)
@method_decorator(name="retrieve", decorator=swagger_auto_schema(operation_summary="detail scientist"))
class ScientistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Scientist.objects.all()
    serializer_class = serializers.ScientistSerializer
    filterset_class = filters.ScientistFilterSet


@method_decorator(
    name="list", decorator=swagger_auto_schema(operation_summary="list musical genres"),
)
class MusicalGenderViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = models.MusicalGender.objects.all()
    serializer_class = serializers.MusicalGenderSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(operation_summary="list occupations"),
)
class OccupationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = models.Occupation.objects.all()
    serializer_class = serializers.OccupationSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(operation_summary="list movie genres"),
)
class MovieGenderViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = models.MovieGender.objects.all()
    serializer_class = serializers.MovieGenderSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(operation_summary="list social medias"),
)
class SocialMediaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = models.SocialMedia.objects.all()
    serializer_class = serializers.SocialMediaSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(operation_summary="list sports"),
)
class SportViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = models.Sport.objects.all()
    serializer_class = serializers.SportSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(operation_summary="list sexual orientations"),
)
class SexualOrientationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = models.SexualOrientation.objects.all()
    serializer_class = serializers.SexualOrientationSerializer


class CountryView(views.APIView):
    permission_classes = [permissions.AllowAny]
    swagger_schema = None

    def get(self, request):
        data = list(
            map(lambda code: {"code": code, "name": countries.countries[code]}, countries.countries.keys())
        )
        results = serializers.CountrySerializer(data, many=True).data
        return response.Response({"count": len(results), "next": None, "previous": None, "results": results})
