from rest_framework.serializers import ModelSerializer
from .models import Speciality, Hospital, Doctor, Banner, FavoriteDoctor, Review
from authentication.serializers import UserSerializer


class SpecialitySerializer(ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'


class CreateHospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name', 'image', 'location', 'specialities']


class ListHospitalSerializer(ModelSerializer):
    specialities = SpecialitySerializer(many=True)

    class Meta:
        model = Hospital
        fields = ['name', 'image', 'location', 'specialities', 'rates']


class CreateDoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['user', 'about', 'years_of_exp', 'speciality', 'work_on_hospital']


class DoctorSerializer(ModelSerializer):
    user = UserSerializer()
    speciality = SpecialitySerializer()
    work_on_hospital = ListHospitalSerializer()

    class Meta:
        model = Doctor
        fields = '__all__'


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class FavoriteDoctorSerializer(ModelSerializer):
    class Meta:
        model = FavoriteDoctor
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
