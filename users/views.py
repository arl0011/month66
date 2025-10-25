from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer, LoginSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth import login
from rest_framework_simplejwt.views import TokenObtainPairView
from .confirmation_service import save_code, check_code


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            code = save_code(user.id)  
            print(f"Код подтверждения для {user.username}: {code}")  
            return Response({"message": "User registered, confirmation code sent"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({"message": "Login successful"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
class ConfirmCodeView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        code = request.data.get("code")

        if not username or not code:
            return Response({"error": "username и code обязательны"}, status=status.HTTP_400_BAD_REQUEST)

        from django.contrib.auth.models import User
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

        if check_code(user.id, code):  
            user.is_active = True
            user.save()
            return Response({"message": "Пользователь успешно подтверждён!"})
        else:
            return Response({"error": "Неверный или истёкший код"}, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
