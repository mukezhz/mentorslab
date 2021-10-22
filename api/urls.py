from django.urls import path, include
from .views import Login, Register


urlpatterns = [
        path('users/', include('users.urls')),
        path('login/', Login.as_view(), name="login"),
        path('register/', Register.as_view(), name="register")
        ]
