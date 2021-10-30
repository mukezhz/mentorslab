from django.urls import path, include
from .views import ForumViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', ForumViewSet, basename="forum")

urlpatterns = [
        path('', include(router.urls))
        ]
