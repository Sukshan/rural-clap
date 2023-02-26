from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.list_category_view.as_view(), name="list"),
    path("create/", views.create_category_view.as_view(), name="create"),
]