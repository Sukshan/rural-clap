from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.list_user_view.as_view(), name="ListAllUsers"),
    path("create/", views.create_user_view.as_view(), name="CreateNewUser"),
    path("update/<int:pk>/", views.update_user_view.as_view(), name ="UpdateAnUser"), 
]