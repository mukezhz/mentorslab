from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework import validators
from ..models import CustomUser, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
                'id',
                'uuid',
                'title',
                'description',
                'languages',
                'country',
                'tags',
                'avatar']

    def save(self, **kwargs):
        context = self.context
        data = self.data
        request = context.get('request')
        user = request.user
        data['user'] = user
        try:
            if user.profile:
                return self.instance
        except ObjectDoesNotExist:
            if user.is_authenticated:
                validated_data = self.validated_data
                validated_data['user'] = user
                if self.instance is not None:
                    self.instance = self.update(self.instance, validated_data)
                else:
                    self.instance = self.create(validated_data)
        return self.instance


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = CustomUser
        fields = [
                'id',
                'uuid',
                'first_name',
                'last_name',
                'role',
                'email',
                'username',
                'profile']

    def validate_username(self, data):
        if data < 5:
            raise validators.ValidationError("Username must be greater than 4 character")
        return data
