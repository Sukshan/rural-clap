from rest_framework import serializers
from .models import employer

class employer_serializer(serializers.ModelSerializer):
    class Meta:
        model = employer
        fields = "__all__"
