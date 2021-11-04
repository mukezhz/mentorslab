from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from users.views.me import MeModelViewset

schema_url_patterns = [
    path('', include('api.urls')),
]

schema_view = get_schema_view(
    title='Mentorslab API',
    url='http://mlabs.mukezhz.ml/',
    # patterns=schema_url_patterns,
    version='0.0.1',
    description='Mentor Labs is a web-based platform that helps to connect interested learners with their particular expertise.'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', include_docs_urls(title="Mentorslab API")),
    path('', schema_view)
]
