from rest_framework import serializers
from rest_framework.response import Response
from .models import Mentorship, MentorshipResponse


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = ('created_at', 'updated_at', 'title', 'background', 'expectation', 'message', 'status', 'mentor_id', 'mentee_id')


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentorship
        fields = ('title', 'message', 'expectation', 'background')

    def save(self, **kwargs):
        context = self.context
        request = context.get('request')
        data = request.data
        user = request.user
        mentor_id = data['mentor_id']
        mentee_id = user.username
        validated_data = self.validated_data
        validated_data['mentor_id'] = mentor_id
        validated_data['mentee_id'] = mentee_id
        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)
        return self.instance


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorshipResponse
        fields = ('date', 'start_tile', 'end_time', 'link', 'message', 'room_id')
