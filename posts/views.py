from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from posts.models import Product
from posts.serializers import ProductSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def ProductApi(request,id=0):
    if request.method=='GET':
        Product = Product.objects.all()
        Product_serializer=ProductSerializer(Product,many=True)
        return JsonResponse(Product_serializer.data,safe=False)
    elif request.method=='POST':
        Product_data=JSONParser().parse(request)
        Product_serializer=ProductSerializer(data=Product_data)
        if Product_serializer.is_valid():
            Product_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        Product_data=JSONParser().parse(request)
        Product=Product.objects.get(id=Product_data['ProductId'])
        Product_serializer=ProductSerializer(Product,data=Product_data)
        if Product_serializer.is_valid():
            Product_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        Product=Product.objects.get(ProductId=id)
        Product.delete()
        return JsonResponse("Deleted Successfully",safe=False)