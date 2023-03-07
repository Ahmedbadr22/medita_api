from django.urls import path
from .views import *

urlpatterns = [
    # Banner
    path('add-banner', CreateBannerAPIView.as_view()),
    path('list-banners', ListBannersAPIView.as_view()),
    # speciality
    path('add-speciality', CreateSpecialityAPIView.as_view()),
    path('list-specialities', ListSpecialityAPIView.as_view()),
    #  favorite-doctor
    path('add-favorite-doctor', CreateFavoriteDoctorAPIView.as_view()),
    path('list-favorite-doctors', ListFavoriteDoctorsAPIView.as_view()),
    # review
    path('add-review', CreateReviewAPIView.as_view()),
    path('list-reviews', ListReviewsAPIView.as_view()),
    # Hospital
    path('add-hospital', CreateHospitalSerializerAPIView.as_view()),
    path('list-hospitals', ListHospitalsAPIView.as_view()),
    # Doctor
    path('add-doctor', CreateDoctorSerializerAPIView.as_view()),
    path('add-doctor-rate', CreateDoctorRateSerializerAPIView.as_view()),
    path('list-doctors', ListDoctorsAPIView.as_view()),
    path('list-doctors-by-speciality/<int:id>', ListDoctorsBySpecialityAPIView.as_view()),
    # Appointment
    path('add-appointment', CreateAppointmentAPIView.as_view()),
    path('list-appointments-by-user/<int:id>', ListAppointmentsByUserId.as_view()),
]
