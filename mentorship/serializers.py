from django.db.models import Q
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import validators
from django.contrib.auth import get_user_model
from .models import Mentorship, MentorshipResponse
from django.db.utils import IntegrityError


USER = get_user_model()


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = (
                'uuid',
                'created_at',
                'updated_at',
                'title',
                'background',
                'expectation',
                'message',
                'status',
                'mentor_id',
                'mentee_id')


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = ('title', 'message', 'expectation', 'background', 'mentor_id')

    def validate_mentor_id(self, data):
        mentee = self.context.get('request').user.username
        datas = Mentorship.objects.filter(
                Q(mentor_id=data) & Q(mentee_id=mentee))
        same = Mentorship.objects.filter(
                Q(mentor_id=data) & Q(mentee_id=mentee))
        try:
            if len(datas) >= 1 or len(same) >= 1:
                raise validators.ValidationError("Request already exists")
        except USER.DoesNotExist:
            raise validators.ValidationError("Mentor doesn't exists")
        return data

    def save(self, **kwargs):
        context = self.context
        request = context.get('request')
        user = request.user
        mentee_id = user.username
        validated_data = self.validated_data
        validated_data['mentee_id'] = mentee_id
        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)
        return self.instance


class AnswerSerializer(serializers.ModelSerializer):
    mentee_id = serializers.CharField(max_length=32)
    class Meta:
        model = MentorshipResponse
        fields = (
                'mentee_id',
                'message',
                'link',
                'date',
                'start_time',
                'end_time',)

    def validate_mentee_id(self, data):
        mentor = self.context.get('request').user.username
        try:
            mentorship = Mentorship.objects.get(Q(mentee_id=data) & Q(mentor_id=mentor))
            return (data, mentorship)
        except Mentorship.DoesNotExist:
            raise validators.ValidationError(f"{data} user has not resquest")

    def save(self, **kwargs):
        context = self.context
        request = context.get('request')
        validated_data = self.validated_data
        validated_data['mentorship'] = validated_data.get('mentee_id')[1]
        validated_data['mentee_id'] = validated_data.get('mentee_id')[0]
        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)
        return self.instance

    def create(self, data):
        mentorship = data.get('mentorship')
        mentee_id = data.get('mentee_id')
        message = data.get('message')
        link = data.get('link')
        date = data.get('date')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        try:
            mentorship_response, status = MentorshipResponse.objects.get_or_create(
               mentorship=mentorship,
               mentee_id=mentee_id,
               message=message,
               link=link,
               date=date,
               start_time=start_time,
               end_time=end_time
                )
        except IntegrityError:
            mentorship_response = MentorshipResponse.objects.get(mentorship=mentorship)
        except MentorshipResponse.DoesNotExist:
            raise validators.ValidationError("unable to create")
        mentorship_response.mentorship = mentorship
        mentorship_response.mentee_id = mentee_id
        mentorship_response.message = message
        mentorship_response.link = link
        mentorship_response.date = date
        mentorship_response.start_time = start_time
        mentorship_response.end_time = end_time
        mentorship_response.save()
        return mentorship_response

    def update(self, instance, data):
        instance.mentorship = data.get('mentorship', instance.membership)
        instance.message = data.get('message', instance.message)
        instance.link = data.get('link', instance.link)
        instance.date = data.get('date', instance.date)
        instance.start_time = data.get('start_time', instance.start_time)
        instance.end_time = data.get('end_time', instance.end_time)
        instance.save()
        return instance


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipResponse
        fields = (
                'uuid',
                'mentorship',
                'message',
                'link',
                'date',
                'start_time',
                'end_time',)


class UpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = 'status',
