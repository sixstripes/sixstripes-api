from invitations import models, serializers
from rest_framework.generics import CreateAPIView


class InviteCreateAPIView(CreateAPIView):
    queryset = models.Invite.objects.all()
    serializer_class = serializers.InviteSerializer
    authentication_classes = []
    permission_classes = []
    swagger_schema = None


class DataSuggestionAPIView(CreateAPIView):
    queryset = models.DataSuggestion.objects.all()
    serializer_class = serializers.DataSuggestionSerializer
    authentication_classes = []
    permission_classes = []
    swagger_schema = None
