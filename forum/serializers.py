import uuid
from rest_framework import serializers
from .models import Forum
from django.contrib.auth import get_user_model

USER = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ['username', 'first_name', 'last_name']


class FormSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Forum
        fields = ['uuid', 'topic', 'body', 'tags', 'author']

    def save(self, **kwargs):
        context = self.context
        request = context.get('request')
        user = request.user
        validated_data = self.validated_data
        instance_uuid = self.instance
        id = instance_uuid.uuid if instance_uuid else uuid.uuid4()
        validated_data['uuid'] = id
        validated_data['author'] = user
        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)
        return self.instance
