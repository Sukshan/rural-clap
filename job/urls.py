from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.list_job_view.as_view(), name="list"),
    path("create/", views.create_job_view.as_view(), name="create"),
    path("read/<int:pk>/", views.read_job_view.as_view(), name="read"),
    path("partial/<int:pk>/", views.UpdateAPIView.as_view(), name="partial"),
    path("update/<int:pk>/", views.update_job_view.as_view(), name="update"),
    path("delete/<int:pk>/", views.delete_job_view.as_view(), name="delete"),
]