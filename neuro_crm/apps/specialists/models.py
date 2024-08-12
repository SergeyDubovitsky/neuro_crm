# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from neuro_crm.core.models import LifetimeInfo

User = get_user_model()


class Speciality(LifetimeInfo):
    name = models.CharField(max_length=120, verbose_name=_("Название"))
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, default=""
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Специализация")
        verbose_name_plural = _("Специализации")


class Specialist(LifetimeInfo):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        verbose_name=_("Пользователь системы"),
        blank=True,
        null=True,
    )
    specialty = models.ForeignKey(
        Speciality,
        on_delete=models.SET_NULL,
        verbose_name=_("Специализация"),
        null=True,
    )
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, default=""
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _("Специалист")
        verbose_name_plural = _("Специалисты")
