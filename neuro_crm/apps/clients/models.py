from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from neuro_crm.core.models import LifetimeInfo

User = get_user_model()


class Client(LifetimeInfo):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Пользователь"),
    )
    full_name = models.CharField(max_length=120, verbose_name=_("ФИО"))
    birth_date = models.DateField(
        null=True, blank=True, verbose_name=_("Дата рождения")
    )
    description = models.TextField(
        verbose_name=_("Описание"),
        blank=True,
        default="",
    )

    class Meta:
        verbose_name = _("Клиент")
        verbose_name_plural = _("Клиенты")

    def __str__(self):
        return self.full_name
