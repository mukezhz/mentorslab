from django.urls import path
from .views import (
        MentorshipApply,
        MentorshipAnswer,
        MentorshipRequestList,
        MentorshipResponseList,
        MentorshipRequestRetrieve,
        MentorshipResponseRetrieve,
        MentorshipStatusUpdate)


urlpatterns = [
        path('apply/<str:username>/', MentorshipApply.as_view() , name="apply"),
        path('answer/<str:username>/', MentorshipAnswer.as_view() , name="answer"),
        path('mentee-requests/', MentorshipRequestList.as_view(), name="requests"),
        path('mentee-requests/<uuid:uuid>/', MentorshipRequestRetrieve.as_view(), name="request"),
        path('mentor-responses/', MentorshipResponseList.as_view(), name="responses"),
        path('mentor-responses/<uuid:uuid>/', MentorshipResponseRetrieve.as_view(), name="response"),
        path('update-status/<uuid:uuid>/', MentorshipStatusUpdate.as_view(), name="update-status"),
        ]
