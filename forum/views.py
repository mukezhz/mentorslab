from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Forum, Comment, Vote, CommentVote
from .serializers import (
        FormSerializer,
        ForumCommentSerializer,
        ForumVoteSerializer,
        ForumCommentVoteSerializer)


class ForumViewSet(ModelViewSet):
    lookup_field = 'uuid'
    queryset = Forum.objects.all()
    serializer_class = FormSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes_by_action = {
    #     "default": [IsAuthenticatedOrReadOnly],
    #     "retrieve": [AllowAny],
    #     "update": [IsAuthenticated],
    # }

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ForumCommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ForumCommentSerializer


class ForumVoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ForumVoteSerializer


class ForumCommentVoteViewSet(ModelViewSet):
    queryset = CommentVote.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ForumCommentVoteSerializer
