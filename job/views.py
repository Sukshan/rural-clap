from django.shortcuts import render
from .serializer import job_serializer
from users.serializer import user_serializer
from .models import job
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers

# Create your views here.
class list_hiring_job_view(generics.ListAPIView):
    serializer_class = job_serializer
    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        status = self.request.query_params.get('status', None)
        queryset = job.objects.filter(category=category,status=status)
        return queryset


class create_job_view(generics.CreateAPIView):
    serializer_class = job_serializer
    queryset = job.objects.all()


class read_job_view(generics.RetrieveAPIView):
    serializer_class = job_serializer
    queryset = job.objects.all()

class update_job_view(generics.UpdateAPIView):
    serializer_class = job_serializer
    queryset = job.objects.all()

class UpdateAPIView(UpdateModelMixin,GenericAPIView):
    serializer_class = job_serializer
    queryset = job.objects.all()
    """
    Concrete view for updating a model instance.
    """
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)



class delete_job_view(generics.DestroyAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = job_serializer
    queryset = job.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return service_provider.objects.filter(user=user)

class list_employer_job_view(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        employerId = int(request.headers.get('Employer'))
        if not employerId:
            return Response({'error': 'Employer Id is Missing'},status=status.HTTP_400_BAD_REQUEST)
        empJob = job.objects.filter(employer=employerId)
        empJobSerialized = job_serializer(empJob, many=True)
        return Response({'data':empJobSerialized.data},status=status.HTTP_200_OK)
