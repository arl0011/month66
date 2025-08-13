from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, obj):
        return obj.products.count()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'reviews','rating']


    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if not reviews.exists():
            return None
        total = sum(review.stars for review in reviews)
        return round(total / reviews.count(), 2)    
