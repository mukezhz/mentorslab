from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer


USER = get_user_model()


class Login(TokenObtainPairView):
    pass


class Register(CreateAPIView):
    queryset = USER.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
