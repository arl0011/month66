from django.urls import path,include
from .views import RegisterView, LoginView, CustomTokenObtainPairView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),  # 🔹 добавлен путь для токена
    path('oauth/', include('social_django.urls', namespace='social')),
]
