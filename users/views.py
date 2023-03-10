from django.shortcuts import render
from .serializer import user_serializer
from .models import users
from rest_framework import generics
from rest_framework import mixins


class list_user_view(generics.ListAPIView):
    serializer_class = user_serializer
    queryset = users.objects.all()

class create_user_view(generics.CreateAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = user_serializer
    queryset = users.objects.all()

class update_user_view(mixins.UpdateModelMixin,generics.GenericAPIView):
    serializer_class = user_serializer
    queryset = users.objects.all()
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)