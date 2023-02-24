from rest_framework import serializers
from .models import service_provider

class service_provider_serializer(serializers.ModelSerializer):
    class Meta:
        model = service_provider
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            kwargs['partial'] = True
            super(service_provider_serializer, self).__init__(*args, **kwargs)