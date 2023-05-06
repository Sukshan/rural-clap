from django.shortcuts import render
from .serializer import job_serializer
from users.serializer import user_serializer
from .models import job
from users import models 
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class list_hiring_job_view(generics.ListAPIView):
    serializer_class = job_serializer
    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        queryset = job.objects.filter(category=category,status='Hiring')
        return queryset


class create_job_view(generics.CreateAPIView):
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

class list_employer_job_view(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        jobData = {}
        userData = {}
        employerId = int(request.headers.get('Employer'))
        print("Employee id is here")
        print(employerId)
        if not employerId:
            return Response({'error': 'Employer Id is Missing'})
        try:
            user = models.users.objects.get(id=employerId)
        except Exception as e:
            user = "No user found"
        if(user!="No user found"):
            serializer = user_serializer(user)
            userData = serializer.data
            if(userData['isEmployer']):
                jobs = job.objects.filter(employer=employerId)
                serializer = job_serializer(jobs, many=True)
                jobData = serializer.data
                return Response({'success':'true', 'jobData' : jobData}, status=status.HTTP_200_OK)
            else:
                return Response({'success':'true', 'userData' : userData}, status=status.HTTP_200_OK)
            
        
        

