from django.shortcuts import render
from .serializer import user_serializer
from .models import users
from rest_framework import generics
from rest_framework import mixins
import pandas as pd
from joblib import load


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
        model = load('model.joblib')
        preprocessor = load('preprocessor.joblib')
        new_user = pd.DataFrame({
            'age': user_data['age'],
            'education': user_data['education'],
            'experience': user_data['experience'],
            'gender': user_data['gender'],
            'job': user_data['category'],
            'skills': user_data['skills'],
        })

        new_user['skills'] = ' '.join(new_user['skills'])
        new_user_encoded = preprocessor.transform(new_user)
        new_user_rating = model.predict(new_user_encoded)
        user_data['modelRating'] = new_user_rating[0]
        serializer.save()


class update_user_view(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = user_serializer
    queryset = users.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
