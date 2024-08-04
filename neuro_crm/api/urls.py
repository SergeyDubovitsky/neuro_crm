from django.urls import path

from neuro_crm.api.healthcheck.views import healthcheck

app_name = "api"

urlpatterns = [
    path("healthcheck", healthcheck, name="healthcheck"),
]
