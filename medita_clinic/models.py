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
)

from authentication.models import User


class Speciality(Model):
    name = CharField(max_length=150)

    # image = ImageField(upload_to='medita_clinic/speciality/')

    def __str__(self):
        return self.name


class Review(Model):
    body = TextField(max_length=600)
    date_of_publish = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Rate(Model):
    by = ForeignKey(User, on_delete=CASCADE)
    star_count = IntegerField(default=0)

    def __str__(self):
        return "{} of 5 by {}".format(self.star_count, self.by.email)


class Hospital(Model):
    name = CharField(max_length=150)
    image = ImageField(upload_to='medita_clinic/hospital/')
    location = CharField(max_length=600)
    rates = ManyToManyField(Rate)
    specialities = ManyToManyField(Speciality)

    def __str__(self):
        return self.name


class Doctor(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    about = TextField(max_length=800)
    years_of_exp = IntegerField(default=0)
    speciality = ForeignKey(Speciality, on_delete=DO_NOTHING)
    work_on_hospital = ForeignKey(Hospital, on_delete=DO_NOTHING)
    rates = ManyToManyField(Rate)

    def __str__(self):
        return self.user.email


class FavoriteDoctor(Model):
    doctor = ForeignKey(Doctor, on_delete=CASCADE)
    patient = ForeignKey(User, on_delete=CASCADE)


class Appointment(Model):
    doctor = ForeignKey(Doctor, on_delete=CASCADE)
    patient = ForeignKey(User, on_delete=CASCADE)
    booking_request_date = DateTimeField(auto_now_add=True)
    appointment_date = DateField()
    appointment_time = TimeField()
    problem_detail = TextField(max_length=1500)
    appointment_status = CharField(max_length=20)
    appointment_summary = TextField(1000)


class Banner(Model):
    title = CharField(max_length=150)
    body = TextField()
    image = ImageField(upload_to='medita_clinic/banners/')
