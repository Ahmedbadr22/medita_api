# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from .predictors import BrainCancerDetector, StomachDiseaseDetector
from medita_clinic.models import Disease
from medita_clinic.serializers import DiseaseSerializer


class BrainCancerDetection(APIView):
    @classmethod
    def post(cls, request):
        file_uploaded = request.FILES.get('image')
        disease_category_id = request.data['disease_category']
        file_name = default_storage.save(file_uploaded.name, file_uploaded)
        file_url = default_storage.url(file_name)
        detector = BrainCancerDetector()
        accuracy, prediction = detector.predict(file_url[1:])

        disease = Disease.objects.filter(classification_label=prediction,
                                         related_disease_category_id=disease_category_id).first()
        serializer = DiseaseSerializer(disease)

        data = {
            'accuracy': accuracy,
            'disease': serializer.data
        }
        return Response(data, status=200)


class StomachCancerDetection(APIView):
    @classmethod
    def post(cls, request):
        file_uploaded = request.FILES.get('image')
        disease_category_id = request.data['disease_category']

        file_name = default_storage.save(file_uploaded.name, file_uploaded)
        file_url = default_storage.url(file_name)
        detector = StomachDiseaseDetector()
        accuracy, prediction = detector.predict(file_url[1:])
        disease = Disease.objects.filter(classification_label=prediction,
                                         related_disease_category_id=disease_category_id).first()
        serializer = DiseaseSerializer(disease)

        data = {
            'accuracy': accuracy,
            'disease': serializer.data
        }
        return Response(data, status=200)
