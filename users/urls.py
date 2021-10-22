from django.urls import path, include
from users.views import me, users
from mentorslab.urls import router

router.register('me', me.MeModelViewset, basename='me')
router.register('users', users.UserModelViewset, basename='user')
router.register('mentors', users.MentorModelViewSet, basename='mentor')
router.register('mentees', users.MenteeModelViewSet, basename='mentor')

urlpatterns = [
        path('', include(router.urls)),
        path('create-profile/', me.CreateProfile.as_view(), name="create-profile")
        ]
