from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import (Speciality, Hospital, Doctor, Banner, FavoriteDoctor, Review, Rate, Appointment, DoctorRate,
                     Disease, DiseaseCategory, PatientDiagnosis)
from authentication.serializers import UserSerializer


# Speciality
class SpecialitySerializer(ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'


# Hospital
class CreateHospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name', 'image', 'location', 'specialities', 'latitude', 'longitude']


class ListHospitalSerializer(ModelSerializer):
    specialities = SpecialitySerializer(many=True)

    class Meta:
        model = Hospital
        fields = '__all__'


# Review
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# Rate
class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


# Doctor
class CreateDoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['user', 'about', 'years_of_exp', 'speciality', 'work_on_hospital']


class UpdateDoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['about', 'years_of_exp', 'speciality', 'work_on_hospital']


class DoctorSerializer(ModelSerializer):
    user = UserSerializer()
    speciality = SpecialitySerializer()
    work_on_hospital = ListHospitalSerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorRatesDistributionSerializer(ModelSerializer):
    one_star_count = SerializerMethodField('get_one_star_count')
    two_star_count = SerializerMethodField('get_two_star_count')
    three_star_count = SerializerMethodField('get_three_star_count')
    four_star_count = SerializerMethodField('get_four_star_count')
    five_star_count = SerializerMethodField('get_five_star_count')

    class Meta:
        model = DoctorRate
        fields = ['one_star_count', 'two_star_count', 'three_star_count', 'four_star_count', 'five_star_count']

    @classmethod
    def get_one_star_count(cls, doctor):
        return DoctorRate.objects.filter(doctor_id=doctor.id, star_count=1).count()

    @classmethod
    def get_two_star_count(cls, doctor):
        return DoctorRate.objects.filter(doctor_id=doctor.id, star_count=2).count()

    @classmethod
    def get_three_star_count(cls, doctor):
        return DoctorRate.objects.filter(doctor_id=doctor.id, star_count=3).count()

    @classmethod
    def get_four_star_count(cls, doctor):
        return DoctorRate.objects.filter(doctor_id=doctor.id, star_count=4).count()

    @classmethod
    def get_five_star_count(cls, doctor):
        return DoctorRate.objects.filter(doctor_id=doctor.id, star_count=5).count()


# Doctor - Rate
class CreateDoctorRateSerializer(ModelSerializer):
    class Meta:
        model = DoctorRate
        fields = '__all__'


# Doctor - Appointment
class ListTodayAuthenticatedDoctorAppointmentsSerializer(ModelSerializer):
    patient = UserSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'


# Banner
class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


# Appointment
class AppointmentSerializer(ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'problem_detail', 'is_canceled', 'booking_request_date']


class CreateAppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'time', 'problem_detail']


# Favorite Doctor
class FavoriteDoctorSerializer(ModelSerializer):
    class Meta:
        model = FavoriteDoctor
        fields = '__all__'


class ListFavoriteDoctorsSerializer(ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = FavoriteDoctor
        fields = ['id', 'doctor']


# Disease
class DiseaseSerializer(ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'


class DiseaseCategorySerializer(ModelSerializer):
    class Meta:
        model = DiseaseCategory
        fields = '__all__'


# Patient Diagnosis
class CreatePatientDiagnosisSerializer(ModelSerializer):
    class Meta:
        model = PatientDiagnosis
        fields = '__all__'


class PatientDiagnosisSerializer(ModelSerializer):
    patient = UserSerializer()
    doctor = DoctorSerializer()
    doctor_diagnosis_disease = DiseaseSerializer()
    predicted_diagnosis = DiseaseSerializer()

    class Meta:
        model = PatientDiagnosis
        fields = '__all__'
