from django.db import models


# class PatientDiseaseDetection(models.Model):
#     disease = models.ForeignKey("medita_clinic.Disease", on_delete=models.CASCADE)
#     disease_image = models.ImageField(upload_to='analytics/disease/classification/')
#     patient = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
#
#
# class RX(models.Model):
#     disease = models.ForeignKey("medita_clinic.Disease", on_delete=models.CASCADE)
#     doctor = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
#     patient = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     note = models.TextField()
#     treatments = models.ManyToManyField("pharmacy.Treatment")





