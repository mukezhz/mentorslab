import uuid
from django.db import IntegrityError
from rest_framework import serializers, validators, status
from .models import Forum, Comment, Vote, CommentVote
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


class MiniForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ['uuid']


class ForumCommentSerializer(serializers.ModelSerializer):
    commentor = AuthorSerializer()
    forum = MiniForumSerializer()

    class Meta:
        model = Comment
        fields = ['forum', 'body', 'commentor']

    def save(self, **kwargs):
        context = self.context
        request = context.get('request')
        data = request.data
        user = request.user
        uid = data.get('forum').get('uuid')
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
        forum = Forum.objects.get(uuid=uuid)
        body = validated_data.get('body')
        commentor_data = validated_data.get('commentor')
        comment = Comment.objects.create(
                forum=forum,
                body=body,
                commentor=commentor_data)
        return comment


class ForumVoteSerializer(serializers.ModelSerializer):
    voter = AuthorSerializer()
    forum = MiniForumSerializer()

    class Meta:
        model = Vote
        fields = ['forum', 'number', 'voter']

    def save(self, **kwargs):
        context = self.context
        request = context.get('request')
        data = request.data
        user = request.user
        uid = data.get('forum').get('uuid')
        validated_data = self.validated_data
        validated_data['voter'] = user
        validated_data['uuid'] = uid
        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)
        return self.instance

    def create(self, validated_data):
        uuid = validated_data.get('uuid')
        forum = Forum.objects.get(uuid=uuid)
        number = validated_data.get('number')
        voter = validated_data.get('voter')
        try:
            if voter.forumvoters.get(forum=forum):
                return
        except Vote.DoesNotExist:
            vote = Vote.objects.create(
                forum=forum,
                number=number,
                voter=voter)
        except IntegrityError:
            raise serializers.ValidationError({
                "msg": "Alreay created"},
                status.HTTP_400_BAD_REQUEST)
        except Exception:
            return
        return vote

    def update(self, instance, data):
        instance.number = data.get('number', instance.number)
        instance.save()
        return instance


class MiniCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'id',


class ForumCommentVoteSerializer(serializers.ModelSerializer):
    voter = AuthorSerializer()
    comment = MiniCommentSerializer()

    class Meta:
        model = Vote
        fields = ['comment', 'number', 'voter']

    def save(self, **kwargs):
        context = self.context
        request = context.get('request')
        data = request.data
        id = data.get('comment').get('id')
        user = request.user
        validated_data = self.validated_data
        validated_data['voter'] = user
        validated_data['id'] = id
        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)
        return self.instance

    def create(self, validated_data):
        id = validated_data.get('id')
        number = validated_data.get('number')
        voter = validated_data.get('voter')
        try:
            comment = Comment.objects.get(id=id)
            if comment.forumcommentvotes.get(voter=voter):
                return
        except CommentVote.DoesNotExist:
            comment_vote = CommentVote.objects.create(
                comment=comment,
                number=number,
                voter=voter)
        except Exception:
            raise validators.ValidationError("Error occcur")
        return comment_vote

    def update(self, instance, data):
        instance.number = data.get('number', instance.number)
        instance.save()
        return instance
