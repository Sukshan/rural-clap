from django.shortcuts import render
from .serializer import category_serializer
from .models import category
from rest_framework import generics

# Create your views here.
class list_category_view(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = category_serializer
    queryset = category.objects.all()


class create_category_view(generics.CreateAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = category_serializer
    queryset = category.objects.all()
