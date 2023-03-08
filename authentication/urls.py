from django.urls import path
from . import views


urlpatterns = [
    path('rest-auth/google/', views.GoogleLogin.as_view(), name='google_login'),
]