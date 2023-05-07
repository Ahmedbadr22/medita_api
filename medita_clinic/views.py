import datetime
from gradio_client import Client

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (FavoriteDoctor, Review, Doctor, Banner, Speciality, Hospital, Appointment, DoctorRate, Disease,
                     DiseaseCategory, PatientDiagnosis)
from .serializers import (
    BannerSerializer,
    SpecialitySerializer,
    FavoriteDoctorSerializer,
    ListHospitalSerializer,
    CreateHospitalSerializer,
    ReviewSerializer,
    CreateDoctorSerializer,
    DoctorSerializer,
    AppointmentSerializer,
    CreateAppointmentSerializer,
    ListFavoriteDoctorsSerializer,
    DoctorRatesDistributionSerializer,
    CreateDoctorRateSerializer,
    ListTodayAuthenticatedDoctorAppointmentsSerializer,
    DiseaseSerializer,
    DiseaseCategorySerializer,
    UpdateDoctorSerializer,
    PatientDiagnosisSerializer,
    CreatePatientPredictionDiagnosisSerializer,
    CreatePatientDiagnosisSerializer
)


# Banner
class CreateBannerAPIView(CreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class DeleteBannerAPIView(DestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    lookup_field = 'id'


class ListBannersAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


# Speciality
class CreateSpecialityAPIView(CreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class DeleteSpecialityAPIView(DestroyAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    lookup_field = 'id'


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


class DeleteHospitalSerializerAPIView(DestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = CreateHospitalSerializer
    lookup_field = "id"


class ListHospitalsAPIView(ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = ListHospitalSerializer


# Doctor
class CreateDoctorSerializerAPIView(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = CreateDoctorSerializer


class DeleteDoctorAPIView(DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'id'


class ListDoctorsAPIView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class ListDoctorsBySpecialityAPIView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'id'

    def get_queryset(self):
        speciality_id = self.kwargs.get(self.lookup_field)
        # return self.queryset.filter(speciality_id=speciality_id).order_by('rates__star_count')
        return self.queryset.filter(speciality_id=speciality_id)


class ListMostRatedDoctorsBySpecialityId(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'id'

    def get_queryset(self):
        speciality_id = self.kwargs.get(self.lookup_field)
        return self.queryset.filter(speciality_id=speciality_id).order_by('rates__star_count')[10:]


class GetDoctorRatesDistributionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = DoctorRatesDistributionSerializer(instance=self.get_queryset())
        return Response(serializer.data, status=200)

    def get_queryset(self):
        user = self.request.user
        doctor = Doctor.objects.filter(user_id=user.id).first()
        return DoctorRate.objects.filter(doctor_id=doctor.id).first()


# TODO: Add List Most rated doctor in every speciality speciality

class UpdateDoctorDetailAPIView(UpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = UpdateDoctorSerializer

    def get_object(self):
        user = self.request.user
        return self.queryset.filter(user_id=user.id).first()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


# Doctor Rate
class CreateDoctorRateAPIVIew(CreateAPIView):
    queryset = DoctorRate.objects.all()
    serializer_class = CreateDoctorRateSerializer


# Doctor - Appointment
class ListTodayAuthenticatedDoctorAppointmentsAPIView(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = ListTodayAuthenticatedDoctorAppointmentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        doctor = Doctor.objects.filter(user_id=user.id).first()
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        return self.queryset.filter(doctor_id=doctor.id, date__range=(today_min, today_max))


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


# Disease
class CreateDiseaseAPIView(CreateAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class ListDiseasesAPIView(ListAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class DeleteDiseaseAPIView(DestroyAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    lookup_field = 'id'


# Disease Category
class CreateDiseaseCategoryAPIView(CreateAPIView):
    queryset = DiseaseCategory.objects.all()
    serializer_class = DiseaseCategorySerializer


class ListDiseaseCategoriesAPIView(ListAPIView):
    queryset = DiseaseCategory.objects.all()
    serializer_class = DiseaseCategorySerializer


class DeleteDiseaseCategoryAPIView(DestroyAPIView):
    queryset = DiseaseCategory.objects.all()
    serializer_class = DiseaseCategorySerializer
    lookup_field = 'id'


# Patient Diagnosis

class CreatePatientDiagnosisAPIView(CreateAPIView):
    queryset = PatientDiagnosis.objects.all()
    serializer_class = CreatePatientDiagnosisSerializer


class ListPatientDiagnosisByPatientIdAPIView(ListAPIView):
    queryset = PatientDiagnosis.objects.all()
    serializer_class = PatientDiagnosisSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_field)
        return self.queryset.filter(patient_id=user_id)


class ListPatientDiagnosisByDoctorIdAPIView(ListAPIView):
    queryset = PatientDiagnosis.objects.all()
    serializer_class = PatientDiagnosisSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_field)
        return self.queryset.filter(doctor_id=user_id)


client = Client("https://ahmedbadrdev-stomach.hf.space/")


class PredictPatientDiagnosisAPIView(CreateAPIView):
    queryset = PatientDiagnosis.objects.all()
    serializer_class = CreatePatientPredictionDiagnosisSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            instance_id = serializer.data["id"]
            image_path = serializer.data["disease_image"]
            result = client.predict(image_path, api_name="/predict")
            label = result[0]
            accuracy = result[1]
            disease = Disease.objects.filter(name=label)
            if disease.exists():
                patent_diagnosis = PatientDiagnosis.objects.filter(instance_id)
                if patent_diagnosis.exists():
                    instance = patent_diagnosis.first()
                    instance.predicted_diagnosis_id = disease.first().id
                    instance.predicted_diagnosis_accuracy = accuracy
                    instance.save()
                    serializer = self.get_serializer(instance)
                    return Response(serializer.data, status=201)
                else:
                    return Response({'detail': 'patient diagnoses not found'}, status=400)
            else:
                return Response({'detail': 'disease not found'}, status=400)
        return Response(serializer.errors, status=400)
