from django.urls import path, include
from users.views import me, users
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register('me', me.MeModelViewset, basename='me')
router.register('mentors', users.MentorModelViewSet, basename='mentor')
router.register('mentees', users.MenteeModelViewSet, basename='mentee')
router.register('', users.UserModelViewset, basename='user')

urlpatterns = [
        path(
            'create-profile/',
            me.CreateProfile.as_view(),
            name="create-profile"
            ),
        path('', include(router.urls)),
        ]
