from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    birthdate = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "phone_number",
            "password",
            "first_name",
            "last_name",
            "birthdate",  # 🔹 добавили поле
        )

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")


# 🔹 Кастомный сериализатор для JWT, чтобы включить birthdate в токен
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['birthdate'] = user.birthdate.isoformat() if user.birthdate else None

        return token
