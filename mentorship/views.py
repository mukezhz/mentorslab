from rest_framework.generics import (
        CreateAPIView,
        ListAPIView,
        RetrieveAPIView,
        UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Mentorship, MentorshipResponse
from .serializers import (
        ApplySerializer,
        AnswerSerializer,
        RequestSerializer,
        ResponseSerializer,
        UpdateStatusSerializer)


class MentorshipApply(CreateAPIView):
    queryset = Mentorship.objects.all()
    serializer_class = ApplySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return self.create(request, *args, **kwargs)
        return Response({"ok": False}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "status": "pending",
            "ok": True
            },
            status=status.HTTP_201_CREATED,
            headers=headers)


class MentorshipAnswer(CreateAPIView):
    queryset = Mentorship.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "status": "success",
            "ok": True
            },
            status=status.HTTP_201_CREATED,
            headers=headers)


class MentorshipRequestList(ListAPIView):
    queryset = Mentorship.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print("request", user)
        try:
            return Mentorship.objects.filter(mentor_id=user.username)
        except Mentorship.DoesNotExist:
            return None


class MentorshipRequestRetrieve(RetrieveAPIView):
    queryset = Mentorship.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'


class MentorshipResponseList(ListAPIView):
    queryset = MentorshipResponse.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        try:
            return MentorshipResponse.objects.filter(mentee_id=user.username)
        except Mentorship.DoesNotExist:
            return None
        except MentorshipResponse.DoesNotExist:
            return None


class MentorshipResponseRetrieve(RetrieveAPIView):
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'

    def get_queryset(self):
        return MentorshipResponse.objects.all()


class MentorshipStatusUpdate(UpdateAPIView):
    serializer_class = UpdateStatusSerializer
    queryset = Mentorship.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'
