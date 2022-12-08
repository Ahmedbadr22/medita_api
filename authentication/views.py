from rest_framework.generics import CreateAPIView
from .serializers import UserCreationSerializer, SuperuserCreationSerializer, DoctorUserCreationSerializer
from .models import User


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
    Create Superuser Api View using email, password, first_name and last_name
    """
    queryset = User.objects.all()
    serializer_class = DoctorUserCreationSerializer
