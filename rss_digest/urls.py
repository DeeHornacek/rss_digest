"""
URL configuration for rss_digest project.
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    ArticleViewSet,
    DigestArticleViewSet,
    DigestViewSet,
    NewsSourceViewSet,
)

# Register API routes using DRF's router
router = DefaultRouter()
router.register(r"api/news_source", NewsSourceViewSet)
router.register(r"api/article", ArticleViewSet)
router.register(r"api/digest", DigestViewSet)
router.register(r"api/digest_article", DigestArticleViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
