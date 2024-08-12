from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from specialists.models import Specialist, Speciality


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "specialty",
        "get_phone",
        "get_email",
    )
    search_fields = ("user__email", "user__phone")
    list_filter = ("specialty",)

    def get_phone(self, obj):
        if obj.user:
            return obj.user.phone

    get_phone.short_description = _("Телефон")

    def get_email(self, obj):
        if obj.user:
            return obj.user.email

    get_email.short_description = "Email"


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
