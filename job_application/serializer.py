from rest_framework import serializers
from .models import job_application

class job_application_serializer(serializers.ModelSerializer):
    class Meta:
        model = job_application
        fields = "__all__"
