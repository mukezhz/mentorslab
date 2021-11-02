from django.urls import path, include
from .views import BlogViewSet, BlogCommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('comments', BlogCommentViewSet, basename="blogcomment")
router.register('', BlogViewSet, basename="blog")

urlpatterns = [
        path('', include(router.urls))
        ]
