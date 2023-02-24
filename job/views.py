from django.shortcuts import render
from .serializer import job_serializer
from .models import job
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.views import APIView
from django.http import JsonResponse
# Create your views here.
class list_job_view(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = job_serializer
    queryset = job.objects.all()


class create_job_view(generics.CreateAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = job_serializer
    queryset = job.objects.all()


class read_job_view(generics.RetrieveAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = job_serializer
    queryset = job.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return job.objects.filter(user=user)


class update_job_view(generics.UpdateAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = job_serializer
    queryset = job.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return service_provider.objects.filter(user=user)

# class update_partial_view(APIView):
#     def get_object(self, pk):
#         return service_provider.objects.get(pk=pk)
#     def patch(self, request, pk):
#         testmodel_object = self.get_object(pk)
#         serializer = job_serializer(testmodel_object, data=request.data, partial=True) # set partial=True to update a data partially
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(code=201, data=serializer.data)
#         return JsonResponse(code=400, data="wrong parameters")

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
