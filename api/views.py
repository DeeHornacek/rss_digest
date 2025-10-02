from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import NewsSource, Article, Digest, DigestArticle
from .serializers import NewsSourceSerializer, ArticleSerializer, DigestSerializer, DigestArticleSerializer
# from .services.assign_vehicle_driver import AssignVehicleDriver


# CRUD
class NewsSourceViewSet(viewsets.ModelViewSet):
    queryset = NewsSource.objects.all()
    serializer_class = NewsSourceSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class DigestViewSet(viewsets.ModelViewSet):
    queryset = Digest.objects.all()
    serializer_class = DigestSerializer


class DigestArticleViewSet(viewsets.ModelViewSet):
    queryset = DigestArticle.objects.all()
    serializer_class = DigestArticleSerializer


# Smart Vehicle Assignment endpoint
class SmartVehicleAssignment(APIView):
    """
    API endpoint to assign a vehicle and driver to a given order.
    """
    def post(self, request, order_id):
        assignment = AssignVehicleDriver(order_id)
        result = assignment.get_assigned_vehicle_driver()
        # serialized_result = ResponseSerializer(result)
        # return Response(serialized_result.data)
