from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SpecialistsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "specialists"
    verbose_name = _("Специалисты")
