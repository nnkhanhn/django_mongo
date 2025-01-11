from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from posts.models import Product, User
from posts.serializers import ProductSerializer, UserSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from drf_yasg import openapi



# Create your views here.
class productApi(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def list(self, request):
        product = list(Product.objects.all().values())
        return Response(product)
    
class userApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def list(self, request):
        user = list(User.objects.all().values())
        return Response(user)
    
@swagger_auto_schema(method='get', operation_description="Retrieve a list of products", responses={200: openapi.Response('List of products')})
@api_view(['GET'])
def function_based(request):
    product = list(Product.objects.all().values())
    return Response(product)
