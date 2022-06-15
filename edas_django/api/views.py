from django.shortcuts import render
import csv
import pandas as pd
from pgcopy import CopyManager
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rawquestion.models import rawquestion
from .serializers import RawQuestionSerializer

fs = FileSystemStorage(location='tmp/')

@api_view(['GET'])
def get_rawquestion(request):
    if request.method == 'GET':
        rawquestion_list = rawquestion.objects.all()
        serializer = RawQuestionSerializer(rawquestion_list, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add_rawquestion(request):

    file = request.FILES["file"]

    csv_content = file.read()
    file_content = ContentFile(csv_content)
    file_name = fs.save(
        "_tmp.csv", file_content
    )
    tmp_file = fs.path(file_name)
    csv_file = open(tmp_file, errors="ignore")
    reader = csv.reader(csv_file)
    next(reader)
    rawquestion_create = []
    for row in enumerate(reader):

        (
            content, 
            difficulty, 
            unit,
        ) = row
        rawquestion_create.append(
            rawquestion(
                content=content, 
                difficulty=difficulty, 
                unit=unit,
            )
        )

    rawquestion.objects.bulk_create(rawquestion_create)

    return Response({"status": "success"})


    # if request.method == 'POST':
    #     serializer = RawQuestionSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
# Create your views here.
