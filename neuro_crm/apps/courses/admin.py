from django.contrib import admin

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "payer", "specialist")
    search_fields = ("id",)
    list_filter = ("specialist",)
    autocomplete_fields = ("payer", "specialist")
