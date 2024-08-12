from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "birth_date")
    search_fields = ("full_name",)
    list_filter = ("birth_date",)
    autocomplete_fields = ("user",)
