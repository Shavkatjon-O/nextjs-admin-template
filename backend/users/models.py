from common.models import BaseModel
from django.contrib.auth.models import AbstractUser
from users.managers import UserManager


class User(AbstractUser, BaseModel):
    email = None
    first_name = None
    last_name = None

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.username
