from django.urls import path

from . import views

urlpatterns = [
    path("", views.CSVDownloadView.as_view(), name="csv"),
]
