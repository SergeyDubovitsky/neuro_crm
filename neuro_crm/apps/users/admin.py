from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as UserAdmin_

User = get_user_model()


class UserAdmin(UserAdmin_):
    model = User
    list_display = (
        "id",
        "email",
        "phone",
        "is_staff",
        "is_active",
        "is_superuser",
        "email_is_confirmed",
        "date_joined",
    )
    list_filter = (
        "is_staff",
        "is_active",
        "is_superuser",
        "email_is_confirmed",
    )
    autocomplete_fields = ("groups",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "middle_name",
                    "last_name",
                    "phone",
                    "email",
                    "password",
                    "email_is_confirmed",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            None,
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "email_is_confirmed",
                ),
            },
        ),
    )
    search_fields = ("email", "phone")
    ordering = ("-id",)


admin.site.register(User, UserAdmin)
