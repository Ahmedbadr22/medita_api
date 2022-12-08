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
    profile_image = ImageField(upload_to='user-profile/', default='default/user_img/default_user.png')
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    birth_date = DateField(null=True, blank=True)
    date_of_joined = DateTimeField(auto_now_add=True)
    is_active = BooleanField(default=True)
    is_superuser = BooleanField(default=False)
    is_doctor = BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
