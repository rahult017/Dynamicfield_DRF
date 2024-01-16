from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
import sys,os
from excel_api.utils import create_dynamic_table

class ExcelUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def read_file(self, file, *args, **kwargs):
        file_extension = file.name.split('.')[-1].lower()
        if file_extension == 'csv':
            data = pd.read_csv(file)
            return data
        elif file_extension in ['xls', 'xlsx']:
            data = pd.read_excel(file)
            return data
        else:
            raise ValueError(f'File format not allowed: {file_extension}')
        
    
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        filename = file.name.split('.')[0].replace(' ', '_')
        if file and hasattr(file, 'name'):
            try:
                df = self.read_file(file)
                create_dynamic_table(filename, df)
                return Response({'message': 'Data successfully inserted'}, status=status.HTTP_200_OK)

            except ValueError as e:
                return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno,str(e))
                return Response({'Error': f"Exception occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
