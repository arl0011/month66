from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny  
from django.contrib.auth.models import User

from .models import Category, Product, Review, UserConfirmation
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from .permissions import IsModerator  


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        user = self.request.user
        if user.is_authenticated and user.is_staff:
            return [IsAuthenticated(), IsModerator()]
        return [AllowAny()]


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def get_permissions(self):
        user = self.request.user
        if user.is_authenticated and user.is_staff:
            return [IsAuthenticated(), IsModerator()]
        return [AllowAny()]


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'


class RegisterUserAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'username, password и email обязательны'}, status=status.HTTP_400_BAD_REQUEST)

        
class ConfirmUserAPIView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request):
        username = request.data.get('username')
        code = request.data.get('code')

        if not username or not code:
            return Response({'error': 'username и code обязательны'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
            confirmation = user.confirmation  
        except User.DoesNotExist:
            return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
        except UserConfirmation.DoesNotExist:
            return Response({'error': 'Подтверждение для пользователя не найдено'}, status=status.HTTP_404_NOT_FOUND)

        if confirmation.code != code:
            return Response({'error': 'Неверный код подтверждения'}, status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()

        confirmation.is_confirmed = True
        confirmation.save()

        return Response({'message': 'Пользователь успешно подтверждён и активирован.'})
