from data import models, serializers
from rest_framework import viewsets


class PoliticianViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Politician.objects.all()
    serializer_class = serializers.PoliticianSerializer
