from rest_framework import serializers
from .models import job_application
from users.serializer import user_serializer
from job.serializer import job_serializer

class job_application_serializer(serializers.ModelSerializer):
    user_id = user_serializer(read_only=True)
    job_id =  job_serializer(read_only=True)
    class Meta:
        model = job_application
        fields = "__all__"
