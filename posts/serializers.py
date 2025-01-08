from rest_framework import serializers
from posts.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product 
        fields=('title','description','created_at','updated_at')