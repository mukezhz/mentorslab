from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserSerializer, ProfileSerializer
from users.models import CustomUser, Profile
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST


class MeModelViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'

    def list(self, request, *args, **kwargs):
        from rest_framework_simplejwt.authentication import JWTAuthentication
        jwt_authentication = JWTAuthentication()
        response = jwt_authentication.authenticate(request)
        # queryset = CustomUser.objects.filter(owner=request.user)
        if request.auth:
            user, token = response
            user_serializer = UserSerializer(user)
            try:
                profile = Profile.objects.get(user=user)
                profile_serializer = ProfileSerializer(profile)
            except ObjectDoesNotExist:
                user = user_serializer.data
                return Response(user)
                # return Response({'msg': 'Profile doesnot exist', 'ok': False}, status=HTTP_404_NOT_FOUND)
            # profile_serializer = ProfileSerializer(profile)
            user = user_serializer.data
            profile = profile_serializer.data
            user['profile'] = profile
            return Response(user)
        return Response({'msg': 'You are not authorized', 'ok': False}, status=HTTP_401_UNAUTHORIZED)


class CreateProfile(CreateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            if user.profile:
                return Response({'msg': 'Profile is already created', 'ok': False}, status=HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            if user.is_authenticated:
                return self.create(request, *args, **kwargs)
        except AttributeError:
            return Response({'msg': 'Login first', 'ok': False}, status=HTTP_401_UNAUTHORIZED)
