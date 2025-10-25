from django.urls import path, include
from .views import RegisterView, LoginView, CustomTokenObtainPairView, ConfirmCodeView
from django.http import HttpResponse

urlpatterns = [
    path("oauth/test/", lambda request: HttpResponse("OAuth path working!")),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"), 
    path("confirm/", ConfirmCodeView.as_view(), name="confirm"),  
    path('oauth/', include('social_django.urls', namespace='social')),
]
