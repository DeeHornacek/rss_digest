from rest_framework import viewsets

from .models import Article, Digest, DigestArticle, NewsSource
from .serializers import (
    ArticleSerializer,
    DigestArticleSerializer,
    DigestSerializer,
    NewsSourceSerializer,
)


class NewsSourceViewSet(viewsets.ModelViewSet):
    """
    CRUD viewset for managing NewsSource objects.
    """

    queryset = NewsSource.objects.all()
    serializer_class = NewsSourceSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    CRUD viewset for managing Article objects.
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class DigestViewSet(viewsets.ModelViewSet):
    """
    CRUD viewset for managing Digest objects.
    """

    queryset = Digest.objects.all()
    serializer_class = DigestSerializer


class DigestArticleViewSet(viewsets.ModelViewSet):
    """
    CRUD viewset for managing DigestArticle objects.
    """

    queryset = DigestArticle.objects.all()
    serializer_class = DigestArticleSerializer
