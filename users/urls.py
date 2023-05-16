from django.urls import path
from . import views
from authentication.decorator import token_required;

urlpatterns = [
    path("list/", views.list_user_view.as_view(), name="ListAllUsers"),
    path("create/",token_required(views.create_user_view.as_view()), name="CreateNewUser"),
    path("update/<int:pk>/", views.update_user_view.as_view(), name ="UpdateAnUser"), 
    path('service-provider/reco/',views.serivce_provider_reco),
    path('service-provider/<int:pk>/applied-jobs/', views.service_provider_appliedjobs.as_view(), name="listofappliedjobs"),
]