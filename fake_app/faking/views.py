import io

import altair as alt
import pandas as pd
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from . import models


class CSVDownloadView(View):
    def get(self, request):
        # request.GET -> url params
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="sample.csv"'

        df = pd.DataFrame(list(models.Book.objects.values()))
        response.write(df.to_csv())
        return response


class ChartView(View):
    def get(self, request):

        df = pd.DataFrame(
            models.Book.objects.values("rating").annotate(count=Count("rating"))
        )
        chart = alt.Chart(df).mark_bar().encode(
            alt.Y("count", title="Number of Books"),
            alt.X("rating", title="Book rating")
        )
        response = HttpResponse()
        chart.save(response, format="html", scale_factor=1.0)
        return response
