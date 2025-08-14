from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, obj):
        return obj.products.count()
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Название категории должно быть не короче 3 символов.")
        
        if Category.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Категория с таким именем уже существует.")

        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Текст отзыва не может быть пустым.")
        return value

    def validate_stars(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Оценка (stars) должна быть от 1 до 5.")
        return value    

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'reviews','rating']


    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Название товара должно быть не короче 3 символов.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше нуля.")
        return value

    def get_reviews(self, obj):
        from .serializers import ReviewSerializer  
        return ReviewSerializer(obj.reviews.all(), many=True).data

    


    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if not reviews.exists():
            return None
        total = sum(review.stars for review in reviews)
        return round(total / reviews.count(), 2)    
