from django.urls import path, include
from . import views


urlpatterns = [
    path('rest-auth/google/', views.GoogleLogin.as_view(), name='google_login'),
]