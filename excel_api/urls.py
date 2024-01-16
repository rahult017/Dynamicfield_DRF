from django.urls import path
from excel_api.views import ExcelUploadView


urlpatterns = [
    path('upload/', ExcelUploadView.as_view(), name='excel-upload'),
]