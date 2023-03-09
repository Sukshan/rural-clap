from django.shortcuts import render
from .serializer import service_provider_serializer
from .models import service_provider
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin



class list_service_provider_view(generics.ListAPIView):
    serializer_class = service_provider_serializer
    queryset = service_provider.objects.all()


class create_service_provider_view(generics.CreateAPIView):

    serializer_class = service_provider_serializer
    queryset = service_provider.objects.all()


class read_service_provider_view(generics.RetrieveAPIView):
    serializer_class = service_provider_serializer
    queryset = service_provider.objects.all()


class update_service_provider_view(generics.UpdateAPIView):
    serializer_class = service_provider_serializer
    queryset = service_provider.objects.all()

class UpdateAPIView(UpdateModelMixin,GenericAPIView):
    
    serializer_class = service_provider_serializer
    queryset = service_provider.objects.all()
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)



class delete_service_provider_view(generics.DestroyAPIView):
    serializer_class = service_provider_serializer
    queryset = service_provider.objects.all()
