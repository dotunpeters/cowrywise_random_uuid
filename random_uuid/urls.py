from django.urls import path

from . import views

app_name = "random_uuid"

urlpatterns = [path("", views.Index.as_view(), name="generate_uuid")]
