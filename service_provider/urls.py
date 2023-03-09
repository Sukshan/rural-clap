from django.urls import path
from . import views
from authentication.decorator import token_required


urlpatterns = [
    path("list/", token_required(views.list_service_provider_view.as_view()), name="list"),
    path("create/", views.create_service_provider_view.as_view(), name="create"),
    path("read/<int:pk>/", views.read_service_provider_view.as_view(), name="read"),
    path("partial/<int:pk>/", views.UpdateAPIView.as_view(), name="partial"),
    path("update/<int:pk>/", views.update_service_provider_view.as_view(), name="update"),
    path("delete/<int:pk>/", views.delete_service_provider_view.as_view(), name="delete"),
]