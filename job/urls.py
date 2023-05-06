from django.urls import path
from . import views
from authentication.decorator import token_required

urlpatterns = [
    path("list/", views.list_hiring_job_view.as_view(), name="list"),
    path("create/", token_required(views.create_job_view.as_view()), name="create"),
    path("list-employer/", token_required(views.list_employer_job_view.as_view()), name="create"),
    path("read/<int:pk>/", views.read_job_view.as_view(), name="read"),
    path("partial/<int:pk>/", views.UpdateAPIView.as_view(), name="partial"),
    path("update/<int:pk>/", views.update_job_view.as_view(), name="update"),
    path("delete/<int:pk>/", views.delete_job_view.as_view(), name="delete"),
]