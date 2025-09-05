from django.contrib import admin
from django.urls import path
from product import views
from .views import (
    CategoryListCreateAPIView, CategoryDetailAPIView,
    ProductListCreateAPIView, ProductDetailAPIView,
    ReviewListCreateAPIView, ReviewDetailAPIView,
    RegisterUserAPIView, ConfirmUserAPIView,
)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('users/register/', RegisterUserAPIView.as_view(), name='user-register'),
    path('users/confirm/', ConfirmUserAPIView.as_view(), name='user-confirm'),
    path('users/login/', obtain_auth_token),
    
    

]
