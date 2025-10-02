from rest_framework import serializers
from .models import NewsSource, Article, Digest, DigestArticle


# Serializer for Orders model - includes all fields
class NewsSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsSource
        fields = '__all__'


# Serializer for Vehicles model - includes all fields
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


# Serializer for Drivers model - includes all fields
class DigestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Digest
        fields = '__all__'


# Serializer for Drivers model - includes all fields
class DigestArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigestArticle
        fields = '__all__'


# Serializer for response, custom dict
class ResponseSerializer(serializers.Serializer):
    assigned_vehicle = serializers.CharField(max_length=100)
    assigned_driver = serializers.CharField(max_length=100)
    estimated_cost = serializers.FloatField()
    distance_km = serializers.FloatField()
    reasoning = serializers.CharField()