from data import models, serializers
from rest_framework import viewsets


class PoliticianViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Politician.objects.all()
    serializer_class = serializers.PoliticianSerializer


class MusicianViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Musician.objects.all()
    serializer_class = serializers.MusicianSerializer


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class DigitalInfluencerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DigitalInfluencer.objects.all()
    serializer_class = serializers.DigitalInfluencerSerializer


class AthletViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Athlet.objects.all()
    serializer_class = serializers.AthletSerializer


class ScientistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Scientist.objects.all()
    serializer_class = serializers.ScientistSerializer
