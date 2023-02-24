from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.list_service_provider_view.as_view(), name="list"),
    path("create/", views.create_service_provider_view.as_view(), name="create"),
    path("read/<int:pk>/", views.read_service_provider_view.as_view(), name="read"),
    path("update/<int:pk>/", views.update_service_provider_view.as_view(), name="update"),
    path("delete/<int:pk>/", views.delete_service_provider_view.as_view(), name="delete"),
]