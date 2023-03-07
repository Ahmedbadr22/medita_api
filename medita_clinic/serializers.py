from rest_framework.serializers import ModelSerializer
from .models import Speciality, Hospital, Doctor, Banner, FavoriteDoctor, Review, Rate, Appointment
from authentication.serializers import UserSerializer


class SpecialitySerializer(ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'


class CreateHospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name', 'image', 'location', 'specialities', 'latitude', 'longitude']


class ListHospitalSerializer(ModelSerializer):
    specialities = SpecialitySerializer(many=True)

    class Meta:
        model = Hospital
        fields = ['name', 'image', 'location', 'specialities', 'latitude', 'longitude']


class CreateDoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['user', 'about', 'years_of_exp', 'speciality', 'work_on_hospital']


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class DoctorSerializer(ModelSerializer):
    user = UserSerializer()
    speciality = SpecialitySerializer()
    work_on_hospital = ListHospitalSerializer()
    reviews = ReviewSerializer(many=True)
    rates = RateSerializer(many=True)

    class Meta:
        model = Doctor
        fields = '__all__'


class CreateDoctorRateSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['rates']


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class AppointmentSerializer(ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'problem_detail', 'is_canceled', 'booking_request_date']


class CreateAppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'time', 'problem_detail']


class FavoriteDoctorSerializer(ModelSerializer):
    class Meta:
        model = FavoriteDoctor
        fields = '__all__'


class ListFavoriteDoctorsSerializer(ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = FavoriteDoctor
        fields = ['id', 'doctor']
