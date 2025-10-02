from rest_framework import serializers

from .models import Article, Digest, DigestArticle, NewsSource


class NewsSourceSerializer(serializers.ModelSerializer):
    """
    Serializer for the NewsSource model, exposing all fields.
    """

    class Meta:
        model = NewsSource
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Article model, exposing all fields.
    """

    class Meta:
        model = Article
        fields = "__all__"


class DigestSerializer(serializers.ModelSerializer):
    """
    Serializer for the Digest model, exposing all fields.
    """

    class Meta:
        model = Digest
        fields = "__all__"


class DigestArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for the DigestArticle model, exposing all fields.
    """

    class Meta:
        model = DigestArticle
        fields = "__all__"

