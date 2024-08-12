from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from specialists.models import Specialist

from neuro_crm.core.models import LifetimeInfo

User = get_user_model()


class Course(LifetimeInfo):
    name = models.CharField(max_length=255, verbose_name=_("Название"))
    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        verbose_name=_("Специалист"),
    )
    payer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("Плательщик")
    )
    start_date = models.DateField(
        verbose_name=_("Дата начала"), blank=True, null=True
    )
    end_date = models.DateField(
        verbose_name=_("Дата окончания"), blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Описание"),
        blank=True,
        default="",
    )

    class Meta:
        verbose_name = _("Курс")
        verbose_name_plural = _("Курсы")

    def __str__(self):
        return self.name


class CourseLesson(LifetimeInfo):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Название"),
        blank=False,
        default="",
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name=_("Курс")
    )
    start_dt = models.DateTimeField(
        verbose_name=_("Время начала"), blank=True, null=True
    )
    end_dt = models.DateTimeField(
        verbose_name=_("Время окончания"), blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, default=""
    )

    class Meta:
        verbose_name = _("Занятие курса")
        verbose_name_plural = _("Занятия курса")

    def __str__(self):
        return self.name
