from django.urls import path

from . import views

urlpatterns = [
    path("csv", views.CSVDownloadView.as_view(), name="csv"),
    path("chart", views.ChartView.as_view(), name="csv"),

]
