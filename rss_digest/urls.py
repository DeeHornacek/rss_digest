"""
URL configuration for rss_digest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import NewsSourceViewSet, ArticleViewSet, DigestViewSet, DigestArticleViewSet

router = DefaultRouter()
router.register(r'api/news_source', NewsSourceViewSet)
router.register(r'api/article', ArticleViewSet)
router.register(r'api/digest', DigestViewSet)
router.register(r'api/digest_article', DigestArticleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]