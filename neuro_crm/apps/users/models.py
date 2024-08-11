from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    email_is_confirmed = models.BooleanField(default=False)
    first_name = None
    last_name = None
    phone = models.CharField(
        _("Телефон"),
        max_length=20,
        blank=True,
        null=True,
        unique=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.id} {self.email}"
