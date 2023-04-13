from django.urls import path
from .views import BrainCancerDetection, StomachCancerDetection

urlpatterns = [
    path('predict-brain-cancer', BrainCancerDetection.as_view()),
    path('predict-stomach-cancer', StomachCancerDetection.as_view()),
]
