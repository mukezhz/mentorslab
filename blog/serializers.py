import uuid
from rest_framework import serializers
from .models import Blog, BlogComment
from django.contrib.auth import get_user_model

USER = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ['username', 'first_name', 'last_name']


class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Blog
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


class MiniBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['uuid']


class BlogCommentSerializer(serializers.ModelSerializer):
    commentor = AuthorSerializer()
    blog = MiniBlogSerializer()

    class Meta:
        model = BlogComment
        fields = ['blog', 'body', 'commentor']

    def save(self, **kwargs):
        context = self.context
        request = context.get('request')
        data = request.data
        user = request.user
        uid = data.get('blog').get('uuid')
        validated_data = self.validated_data
        validated_data['commentor'] = user
        validated_data['uuid'] = uid
        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)
        return self.instance

    def create(self, validated_data):
        uuid = validated_data.pop('uuid')
        blog = Blog.objects.get(uuid=uuid)
        body = validated_data.get('body')
        commentor_data = validated_data.get('commentor')
        comment = BlogComment.objects.create(
                blog=blog,
                body=body,
                commentor=commentor_data)
        return comment
