from django.urls import path
from .views import UserCreationAPIView, SuperuserCreationAPIView, DoctorUserCreationAPIView, IsDoctorUserAPIView, IsFillAllDoctorDataAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView, TokenVerifyView

urlpatterns = [
    path('user-register', UserCreationAPIView.as_view(), name='normal_user_registration'),
    path('admin-register', SuperuserCreationAPIView.as_view(), name='superuser_registration'),
    path('doctor-register', DoctorUserCreationAPIView.as_view()),
    path('login', TokenObtainPairView.as_view(), name='obtain_token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/varify', TokenVerifyView.as_view(), name='token_varify'),
    path('token/block', TokenBlacklistView.as_view(), name='token_block'),
    path('is-doctor-user', IsDoctorUserAPIView.as_view()),
    path('is-fill-all-doctor-data', IsFillAllDoctorDataAPIView.as_view()),
]
