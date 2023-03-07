from django.urls import path
from .views import BrainCancerDetection

urlpatterns = [
    path('predict-brain-cancer', BrainCancerDetection.as_view())
]
