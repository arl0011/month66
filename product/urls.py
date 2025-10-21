from django.contrib import admin
from django.urls import path
from product import views
from users.views import RegisterView, LoginView, CustomTokenObtainPairView
from product.views import ConfirmUserAPIView
from rest_framework.authtoken.views import obtain_auth_token  # можно убрать, если не используешь TokenAuth

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:id>/', views.CategoryDetailAPIView.as_view(), name='category-detail'),
    path('products/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:id>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('reviews/', views.ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view(), name='review-detail'),

    # Пользовательские маршруты
    path('users/register/', RegisterView.as_view(), name='user-register'),
    path('users/confirm/', ConfirmUserAPIView.as_view(), name='user-confirm'),

    
    path('users/login/', LoginView.as_view(), name='user-login'),

    # Получение JWT токенов с birthdate
    path('users/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
