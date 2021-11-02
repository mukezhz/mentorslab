from django.urls import path, include
from .views import (
        ForumViewSet,
        ForumCommentViewSet,
        ForumVoteViewSet,
        ForumCommentVoteViewSet)
from rest_framework.routers import DefaultRouter, SimpleRouter


router = DefaultRouter()
simple = SimpleRouter()
simple.register('votes', ForumCommentVoteViewSet, basename="forumcommentvote")
router.register('comments', ForumCommentViewSet, basename="forumcomment")
router.register('votes', ForumVoteViewSet, basename="forumvote")
router.register('', ForumViewSet, basename="forum")

urlpatterns = [
        path('comments/', include(simple.urls)),
        path('', include(router.urls)),
        ]
