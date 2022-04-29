from django.shortcuts import render
from django.db.models.query import QuerySet
from rest_framework import viewsets
from .serializers import CosineSimilaritySerializer
from .models import cosinesimilarity


# Create your views here.
class cosinesimilarity(viewsets.ModelViewSet):
        serializer_class = CosineSimilaritySerializer
        queryset = cosinesimilarity.objects.all()