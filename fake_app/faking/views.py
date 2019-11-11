from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import pandas as pd
from . import models


class CSVDownloadView(View):
    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="somefilename.csv"'

        df = pd.DataFrame(list(models.Book.objects.values()))
        response.write(df.to_csv())
        return response
