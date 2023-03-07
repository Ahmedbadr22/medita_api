from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import FavoriteDoctor, Review, Doctor, Banner, Speciality, Hospital, Appointment
from .serializers import (
    BannerSerializer,
    SpecialitySerializer,
    FavoriteDoctorSerializer,
    ListHospitalSerializer,
    CreateHospitalSerializer,
    ReviewSerializer,
    CreateDoctorSerializer,
    DoctorSerializer,
    CreateDoctorRateSerializer,
    AppointmentSerializer,
    CreateAppointmentSerializer,
    ListFavoriteDoctorsSerializer
)


# Banner
class CreateBannerAPIView(CreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class ListBannersAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


# Speciality
class CreateSpecialityAPIView(CreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class ListSpecialityAPIView(ListAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


# Favorite
class CreateFavoriteDoctorAPIView(CreateAPIView):
    queryset = FavoriteDoctor.objects.all()
    serializer_class = FavoriteDoctorSerializer


class ListFavoriteDoctorsAPIView(ListAPIView):
    queryset = FavoriteDoctor.objects.all()
    serializer_class = ListFavoriteDoctorsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(patient_id=user.id)


# Review
class CreateReviewAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ListReviewsAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# Hospital
class CreateHospitalSerializerAPIView(CreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = CreateHospitalSerializer


class ListHospitalsAPIView(ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = ListHospitalSerializer


# Doctor
class CreateDoctorSerializerAPIView(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = CreateDoctorSerializer


class CreateDoctorRateSerializerAPIView(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = CreateDoctorRateSerializer


class ListDoctorsAPIView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class ListDoctorsBySpecialityAPIView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'id'

    def get_queryset(self):
        speciality_id = self.kwargs.get(self.lookup_field)
        return self.queryset.filter(speciality_id=speciality_id).order_by('rates__star_count')


class ListMostRatedDoctorsBySpecialityId(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'id'

    def get_queryset(self):
        speciality_id = self.kwargs.get(self.lookup_field)
        return self.queryset.filter(speciality_id=speciality_id).order_by('rates__star_count')[10:]


# TODO: Add List Most rated doctor in every speciality speciality

# Appointment

class CreateAppointmentAPIView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = CreateAppointmentSerializer


class ListAppointmentsByUserId(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_field)
        return self.queryset.filter(patient_id=user_id).order_by('date')
