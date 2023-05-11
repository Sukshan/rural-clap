from rest_framework import serializers
from .models import job
from users.serializer import user_serializer


class job_serializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = "__all__"
        extra_kwargs = {"service_provider": {"required": False, "allow_null": True}, "category": {"required": False, "allow_null": True}, }
        many = True
