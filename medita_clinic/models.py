from django.db.models import (
    Model,
    CharField,
    ImageField,
    TextField,
    IntegerField,
    ForeignKey,
    ManyToManyField,
    DateTimeField,
    TimeField,
    DateField,
    CASCADE,
    DO_NOTHING,
    BooleanField,
    FileField,
    FloatField
)

from authentication.models import User


class Speciality(Model):
    name = CharField(max_length=150, unique=True)
    icon = FileField(upload_to='medita_clinic/specialties')

    def __str__(self):
        return self.name


class Review(Model):
    body = TextField(max_length=600)
    date_of_publish = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Rate(Model):
    """
    notice : remember to change this class to hospital rate
    by add hospital id
    """
    by = ForeignKey(User, on_delete=CASCADE)
    star_count = IntegerField(default=0)

    def __str__(self):
        return "{} of 5 by {}".format(self.star_count, self.by.email)


class Hospital(Model):
    name = CharField(max_length=150)
    image = ImageField(upload_to='medita_clinic/hospital/')
    location = CharField(max_length=600)
    latitude = FloatField(default=0.0)
    longitude = FloatField(default=0.0)
    rates = ManyToManyField(Rate)
    specialities = ManyToManyField(Speciality)

    def __str__(self):
        return self.name


class Doctor(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    about = TextField(max_length=800)
    years_of_exp = IntegerField(default=0)
    speciality = ForeignKey(Speciality, on_delete=DO_NOTHING, null=True, blank=True)
    work_on_hospital = ForeignKey(Hospital, on_delete=DO_NOTHING, null=True, blank=True)
    reviews = ManyToManyField(Review)

    def __str__(self):
        return self.user.email


class DoctorRate(Model):
    doctor = ForeignKey(Doctor, on_delete=CASCADE)
    by = ForeignKey(User, on_delete=CASCADE)
    star_count = IntegerField(default=0)


class FavoriteDoctor(Model):
    doctor = ForeignKey(Doctor, on_delete=CASCADE)
    patient = ForeignKey(User, on_delete=CASCADE)


class Appointment(Model):
    doctor = ForeignKey(Doctor, on_delete=CASCADE)
    patient = ForeignKey(User, on_delete=CASCADE)
    booking_request_date = DateTimeField(auto_now_add=True)
    date = DateField()
    time = TimeField()
    is_canceled = BooleanField(default=False)
    problem_detail = TextField(max_length=1500)
    appointment_report = TextField()
    meeting_link = TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.patient.fullname} has appointment with Doctor: {self.doctor.user.fullname} at {self.date}"


class Banner(Model):
    title = CharField(max_length=150)
    body = TextField()
    image = ImageField(upload_to='medita_clinic/banners/')


class DiseaseCategory(Model):
    name = CharField(max_length=100, unique=True)


class Disease(Model):
    name = CharField(max_length=100, unique=True)
    image = ImageField(upload_to='analytics/disease/images/')
    classification_label = IntegerField(default=0)
    related_disease_category = ForeignKey(DiseaseCategory, on_delete=CASCADE)
    detail = TextField()

