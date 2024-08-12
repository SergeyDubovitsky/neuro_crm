from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager

from neuro_crm.core.models import LifetimeInfo, Person


class User(AbstractUser, LifetimeInfo, Person):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    email_is_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        full_name = f"{self.last_name} {self.first_name} {self.middle_name}"
        return full_name.strip() or self.email

    def __str__(self):
        return self.get_full_name()
