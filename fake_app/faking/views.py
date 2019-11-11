from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import pandas as pd
from . import models
import altair as alt
import io


class CSVDownloadView(View):
    def get(self, request):
        # request.GET -> url params
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="somefilename.csv"'

        df = pd.DataFrame(list(models.Book.objects.values()))
        response.write(df.to_csv())
        return response


class ChartView(View):
    def get(self, request):
        # df = pd.DataFrame(list(models.Book.objects.values()))
        df = pd.DataFrame({"a": list("CCCDDDEEE"), "b": [2, 7, 4, 1, 2, 6, 8, 4, 7]})
        chart = alt.Chart(df).mark_bar().encode(x="a", y="average(b)")
        response = HttpResponse()
        chart.save(response, format="html", scale_factor=1.0)
        return response
