from rest_framework.serializers import ModelSerializer
from .models import User
from medita_clinic.models import Doctor


class UserCreationSerializer(ModelSerializer):
    """
    Normal User Creation Serializer by 'email', 'password', 'first_name', 'last_name'
    """

    class Meta:
        model = User
        fields = ['email', 'password', 'fullname']

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


class SuperuserCreationSerializer(ModelSerializer):
    """
    Superuser Creation Serializer by 'email', 'password', 'first_name', 'last_name'
    """

    class Meta:
        model = User
        fields = ['profile_image', 'email', 'password', 'fullname', 'birth_date']

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_superuser(**validated_data)
        user.save()
        return user


class DoctorUserCreationSerializer(ModelSerializer):
    """
    Doctor user Creation Serializer by 'email', 'password', 'first_name', 'last_name'
    """

    class Meta:
        model = User
        fields = ['profile_image', 'email', 'password', 'fullname', 'birth_date']

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_doctor_user(**validated_data)
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.save()
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_image', 'email', 'fullname', 'birth_date']
