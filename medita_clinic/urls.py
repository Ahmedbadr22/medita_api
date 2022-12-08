from django.urls import path
from .views import *
urlpatterns = [
    # POST Requests
    path('add-banner', CreateBannerAPIView.as_view()),
    path('add-speciality', CreateSpecialityAPIView.as_view()),
    path('add-favorite-doctor', CreateFavoriteDoctorAPIView.as_view()),
    path('add-review', CreateReviewAPIView.as_view()),
    path('add-hospital', CreateHospitalSerializerAPIView.as_view()),
    path('add-doctor', CreateDoctorSerializerAPIView.as_view()),
    # List Requests
    path('list-banners', ListBannersAPIView.as_view()),
    path('list-specialities', ListSpecialityAPIView.as_view()),
    path('list-favorite-doctors', ListFavoriteDoctorsAPIView.as_view()),
    path('list-reviews', ListReviewsAPIView.as_view()),
    path('list-hospitals', ListHospitalsAPIView.as_view()),
    path('list-doctors', ListDoctorsAPIView .as_view()),
]
