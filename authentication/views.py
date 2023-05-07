from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import (UserCreationSerializer, SuperuserCreationSerializer, DoctorUserCreationSerializer)
from .models import User
from medita_clinic.models import Doctor


# Normal user creation
class UserCreationAPIView(CreateAPIView):
    """
    Create Normal User Api View using email, password, first_name and last_name
    """
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer


# superuser creation
class SuperuserCreationAPIView(CreateAPIView):
    """
    Create Superuser Api View using email, password, first_name and last_name
    """
    queryset = User.objects.all()
    serializer_class = SuperuserCreationSerializer


# Doctor user creation
class DoctorUserCreationAPIView(CreateAPIView):
    """
    Create Doctor user Api View using email, password, first_name and last_name
    """
    queryset = User.objects.all()
    serializer_class = DoctorUserCreationSerializer


class IsDoctorUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @classmethod
    def get(cls, request):
        user = request.user
        if user is not None:
            return Response({'is_doctor': user.is_doctor})
        return Response({'detail', 'Not found'}, status=400)


class IsFillAllDoctorDataAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @classmethod
    def get(cls, request):
        user = request.user
        is_found = Doctor.objects.filter(user_id=user.id).exists()
        return Response({'is_found': is_found})
