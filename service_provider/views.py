from django.shortcuts import render
from .serializer import service_provider_serializer
from .models import service_provider
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin

# Create your views here.
class list_service_provider_view(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = service_provider_serializer
    queryset = service_provider.objects.all()


class create_service_provider_view(generics.CreateAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = service_provider_serializer
    queryset = service_provider.objects.all()


class read_service_provider_view(generics.RetrieveAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = service_provider_serializer
    queryset = service_provider.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return service_provider.objects.filter(user=user)


class update_service_provider_view(generics.UpdateAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = service_provider_serializer
    queryset = service_provider.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return service_provider.objects.filter(user=user)


class delete_service_provider_view(generics.DestroyAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = service_provider_serializer
    queryset = service_provider.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return service_provider.objects.filter(user=user)