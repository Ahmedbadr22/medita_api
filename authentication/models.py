from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager
from django.db.models import (
    EmailField,
    CharField,
    DateTimeField,
    ImageField,
    BooleanField,
    DateField,
    Model,
)


class User(AbstractBaseUser):
    email = EmailField(unique=True)
    profile_image = ImageField(upload_to='user-profile/', null=True, blank=True)
    fullname = CharField(max_length=255)
    birth_date = DateField(null=True, blank=True)
    date_of_joined = DateTimeField(auto_now_add=True)
    is_active = BooleanField(default=True)
    is_superuser = BooleanField(default=False)
    is_doctor = BooleanField(default=False)
    gender = BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
