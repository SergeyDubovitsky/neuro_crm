from django.db import models
from django.utils.translation import gettext_lazy as _


class LifetimeInfo(models.Model):
    """An abstract class that adds lifetime values."""

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True


class Person(models.Model):
    last_name = models.CharField(
        _("Фамилия"), max_length=150, blank=True, default=""
    )
    first_name = models.CharField(
        _("Имя"), max_length=150, blank=True, default=""
    )
    middle_name = models.CharField(
        _("Отчество"), max_length=150, blank=True, default=""
    )
    phone = models.CharField(
        _("Телефон"),
        max_length=20,
        blank=True,
        null=True,
        unique=True,
    )
    birth_date = models.DateField(
        null=True, blank=True, verbose_name=_("Дата рождения")
    )

    class Meta:
        abstract = True
