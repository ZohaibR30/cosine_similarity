from rest_framework import serializers
from .models import cosinesimilarity

class CosineSimilaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = cosinesimilarity
        fields = ('link','title','text', 'angle')