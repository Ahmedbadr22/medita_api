from django.urls import path
from .views import *

urlpatterns = [
    # Banner
    path('add-banner', CreateBannerAPIView.as_view()),
    path('list-banners', ListBannersAPIView.as_view()),
    path('delete-banner/<int:id>', DeleteBannerAPIView.as_view()),
    # speciality
    path('add-speciality', CreateSpecialityAPIView.as_view()),
    path('list-specialities', ListSpecialityAPIView.as_view()),
    path('delete-speciality/<int:id>', DeleteSpecialityAPIView.as_view()),
    #  favorite-doctor
    path('add-favorite-doctor', CreateFavoriteDoctorAPIView.as_view()),
    path('list-favorite-doctors', ListFavoriteDoctorsAPIView.as_view()),
    # review
    path('add-review', CreateReviewAPIView.as_view()),
    path('list-reviews', ListReviewsAPIView.as_view()),
    # Hospital
    path('add-hospital', CreateHospitalSerializerAPIView.as_view()),
    path('delete-hospital/<int:id>', DeleteHospitalSerializerAPIView.as_view()),
    path('list-hospitals', ListHospitalsAPIView.as_view()),
    # Doctor
    path('add-doctor', CreateDoctorSerializerAPIView.as_view()),
    path('update-doctor-detail', UpdateDoctorDetailAPIView.as_view()),
    path('list-doctors', ListDoctorsAPIView.as_view()),
    path('list-doctors-by-speciality/<int:id>', ListDoctorsBySpecialityAPIView.as_view()),
    # Doctor - Rate
    path('add-doctor-rate', CreateDoctorRateAPIVIew.as_view()),
    path('get-authenticated-doctor-rate-distribution', GetDoctorRatesDistributionAPIView.as_view()),
    path('list-today-auth-doctor-appointments', ListTodayAuthenticatedDoctorAppointmentsAPIView.as_view()),
    # Appointment
    path('add-appointment', CreateAppointmentAPIView.as_view()),
    path('list-appointments-by-user/<int:id>', ListAppointmentsByUserId.as_view()),
    # Disease
    path('add-disease', CreateDiseaseAPIView.as_view()),
    path('delete-disease/<int:id>', DeleteDiseaseAPIView.as_view()),
    path('list-diseases', ListDiseasesAPIView.as_view()),
    # Disease category
    path('add-disease-category', CreateDiseaseCategoryAPIView.as_view()),
    path('delete-disease-category/<int:id>', DeleteDiseaseCategoryAPIView.as_view()),
    path('list-disease-categories', ListDiseaseCategoriesAPIView.as_view()),
]
