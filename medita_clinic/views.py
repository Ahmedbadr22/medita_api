from rest_framework.generics import CreateAPIView, ListAPIView
from .models import FavoriteDoctor, Review, Doctor, Banner, Speciality, Hospital
from .serializers import (
    BannerSerializer,
    SpecialitySerializer,
    FavoriteDoctorSerializer,
    ListHospitalSerializer,
    CreateHospitalSerializer,
    ReviewSerializer,
    CreateDoctorSerializer,
    DoctorSerializer
)


class CreateBannerAPIView(CreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class CreateSpecialityAPIView(CreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class CreateFavoriteDoctorAPIView(CreateAPIView):
    queryset = FavoriteDoctor.objects.all()
    serializer_class = FavoriteDoctorSerializer


class CreateReviewAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CreateHospitalSerializerAPIView(CreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = CreateHospitalSerializer


class CreateDoctorSerializerAPIView(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = CreateDoctorSerializer


class ListBannersAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class ListSpecialityAPIView(ListAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class ListFavoriteDoctorsAPIView(ListAPIView):
    queryset = FavoriteDoctor.objects.all()
    serializer_class = FavoriteDoctorSerializer


class ListReviewsAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ListHospitalsAPIView(ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = ListHospitalSerializer


class ListDoctorsAPIView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
