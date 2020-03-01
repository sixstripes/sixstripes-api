from invitations import models, serializers
from rest_framework.generics import CreateAPIView


class InviteCreateAPIView(CreateAPIView):
    queryset = models.Invite.objects.all()
    serializer_class = serializers.InviteSerializer
    authentication_classes = []
    permission_classes = []
