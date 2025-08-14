from django.contrib import admin
from django.urls import path
from product import views
from .views import category_list_create_api_view, category_detail_api_view, product_list_create_api_view, product_detail_api_view,review_list_create_api_view,review_detail_api_view


urlpatterns = [
    path('categories/', views.category_list_api_view),
    path('categories/<int:id>/', views.category_detail_api_view),

    path('products/', views.product_list_api_view),
    path('products/<int:id>/', views.product_detail_api_view),

    path('reviews/', views.review_list_api_view),
    path('reviews/<int:id>/', views.review_detail_api_view),
    path('products/reviews/', views.products_with_reviews),
    path('categories/', views.category_list_api_view),
    path('categories/', category_list_create_api_view),
    path('categories/<int:id>/', category_detail_api_view),
    path('products/', product_list_create_api_view),
    path('products/<int:id>/', product_detail_api_view),
    path('reviews/', review_list_create_api_view),
    path('reviews/<int:id>/', review_detail_api_view),

]
