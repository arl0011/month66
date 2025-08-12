from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response({'error': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ReviewSerializer(review)
    return Response(serializer.data)
