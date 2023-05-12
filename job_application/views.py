from django.shortcuts import render
from .serializer import job_application_serializer
from .models import job_application
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status


class list_job_application_view(generics.ListAPIView):
    serializer_class = job_application_serializer
    # queryset = job_application.objects.all()
    def get_queryset(self):
        job_id = self.request.query_params.get('id', None)
        if job_id is None:
            return Response({'error': 'job_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = job_application.objects.filter(job_id=job_id)
        return queryset
    

class create_job_application_view(generics.CreateAPIView):
    serializer_class = job_application_serializer
    queryset = job_application.objects.all()
    def perform_create(self, serializer):
        # Extract the relevant data from the serializer
        data = serializer.validated_data
        userId = data['user_id']
        jobId = data['job_id']
        print(jobId,userId)
        # Check if the record already exists in the database
        if job_application.objects.filter(user_id=userId, job_id=jobId).exists():
            raise ValidationError('This job application already exists')

        # If the record doesn't exist, create a new one
        serializer.save()


class read_job_application_view(generics.RetrieveAPIView):
    serializer_class = job_application_serializer
    queryset = job_application.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return job.objects.filter(user=user)


class update_job_application_view(generics.UpdateAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = job_application_serializer
    queryset = job_application.objects.all()

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
    serializer_class = job_application_serializer
    queryset = job_application.objects.all()
    """
    Concrete view for updating a model instance.
    """
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)



class delete_job_application_view(generics.DestroyAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = job_application_serializer
    queryset = job_application.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return service_provider.objects.filter(user=user)
    
class service_provider_applied_jobs(generics.ListAPIView):
    serializer_class = job_application_serializer
    def get_queryset(self):
        user_id = self.request.query_params.get('id', None)
        if user_id is None:
            return Response({'error': 'user_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        queryset = job_application.objects.filter(user_id=user_id)
        return queryset