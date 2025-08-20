from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Category, Product, Review, UserConfirmation
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


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


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


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

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Пользователь с таким именем уже существует'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = False  # неактивен до подтверждения
        user.save()

        confirmation = UserConfirmation.objects.create(user=user)
        confirmation.save()

        return Response({'message': 'Пользователь зарегистрирован. Подтвердите аккаунт с помощью кода.', 'code': confirmation.code}, status=status.HTTP_201_CREATED)


class ConfirmUserAPIView(APIView):
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
