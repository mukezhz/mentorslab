from django.db.models import Q
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.api.serializers import UserSerializer
from users.models import CustomUser


class UserModelViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'username'
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class MentorModelViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(Q(role="Mentor"))


class MenteeModelViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(Q(role="Mentee"))
