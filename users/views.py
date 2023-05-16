from django.shortcuts import render
from django.views import View
from .serializer import user_serializer
from .models import users
from rest_framework import generics
from rest_framework import mixins
import pandas as pd
from joblib import load
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from users.models import users
from django.core import serializers
from job.models import job
from django.shortcuts import get_object_or_404
from job.serializer import job_serializer

model_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'model.joblib')
preprocessor_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'preprocessor.joblib')


class list_user_view(generics.ListAPIView):
    serializer_class = user_serializer
    queryset = users.objects.all()


class create_user_view(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = user_serializer
    queryset = users.objects.all()

    def perform_create(self, serializer):
        # Retrieve the validated data
        user_data = serializer.validated_data

        # Modify the validated data as needed
        # For example, to set a default value for a field:
        if user_data['isEmployer'] == False:
            model = load(model_path)
            preprocessor = load(preprocessor_path)
            index = [0]
            new_user = pd.DataFrame({
                'age': user_data['age'],
                'education': user_data['education'],
                'experience': user_data['experience'],
                'gender': user_data['gender'],
                'job': user_data['category'],
                'skills': user_data['skills'],
            }, index=index)
            new_user['skills'] = new_user['skills'].str.split(',')
            new_user['skills'] = ' '.join(
                [str(skill) for skill in new_user['skills']])
            new_user_encoded = preprocessor.transform(new_user)
            new_user_rating = model.predict(new_user_encoded)
            user_data['modelRating'] = new_user_rating[0]
        serializer.save()


class update_user_view(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = user_serializer
    queryset = users.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


@api_view(["GET"])
def serivce_provider_reco(request, *args, **kwargs):
    language = request.GET.get('language', None)
    location = request.GET.get('location', None)
    category = request.GET.get('category', None)
    reco = users.objects.filter(
        isEmployer=False, language=language, location=location, category=category).order_by('-modelRating')
    data = serializers.serialize('json', reco)
    print(data)
    return Response({"message": "reco from user", 'data': data}, status=status.HTTP_200_OK)


class service_provider_appliedjobs(generics.ListAPIView):
    serializer_class = job_serializer
    def get_queryset(self):
        user = get_object_or_404(users, id=self.kwargs['pk'])
        applied_jobs = user.applied_jobs.split()
        applied_jobs = list(map(int, applied_jobs))
        queryset = job.objects.filter(pk__in=applied_jobs)
        return queryset    