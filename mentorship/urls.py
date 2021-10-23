from django.urls import path, include
from mentorslab.urls import router
from .views import MentorshipApply


urlpatterns = [
        path('apply/<str:username>/', MentorshipApply.as_view() , name="apply"),
        ]
