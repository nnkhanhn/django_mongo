from rest_framework import serializers
from posts.models import Product, User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product 
        fields=('title','description','created_at','updated_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields='__all__'