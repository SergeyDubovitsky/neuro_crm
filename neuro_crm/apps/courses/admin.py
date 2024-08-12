from django.contrib import admin

from .models import Course, CourseLesson


class CourseLessonInline(admin.TabularInline):
    model = CourseLesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "payer", "specialist")
    search_fields = ("id",)
    list_filter = ("specialist", "payer")
    autocomplete_fields = ("payer", "specialist")
    inlines = (CourseLessonInline,)
