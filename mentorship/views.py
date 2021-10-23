import json
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Mentorship
from .serializers import ApplySerializer



class MentorshipApply(CreateAPIView):
    queryset = Mentorship.objects.all()
    serializer_class = ApplySerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = request.user
        mentor = kwargs.get('username')
        data = request.data
        data['mentor_id'] = mentor
        if user.is_authenticated:
            return self.create(request, *args, **kwargs)
        return Response({"ok": False}, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        serializer = ApplySerializer(data=request.data,)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": "pending", "ok": True}, status=status.HTTP_201_CREATED, headers=headers)
