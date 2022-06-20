from django.shortcuts import render
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import viewsets
from rawquestion.models import RawQuestion
from questiongenerator.models import *
from .serializers import RawQuestionSerializer
from .serializers import QuestionSerializer, QuestionSetSerializer, QuestionPaperSerializer, QuestionPaperSetSerializer, AcademicYearSerializer, CourseSerializer, ExamSerializer, ExamNoteSerializer, SubjectSerializer

fs = FileSystemStorage(location='tmp/')

class RawQuestionViewSet(viewsets.GenericViewSet, 
                mixins.RetrieveModelMixin, 
                mixins.ListModelMixin
    ):
    queryset = RawQuestion.objects.all()
    serializer_class = RawQuestionSerializer

    def create(self, request):
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
        for id_,row in enumerate(reader):
            (
                content, 
                difficulty, 
                unit,

            ) = row

            rawquestion_create.append(
                RawQuestion(
                    content=content, 
                    difficulty=difficulty, 
                    unit=unit,
                )
            )

        RawQuestion.objects.bulk_create(rawquestion_create)

        return Response({"status": "success"})

class QuestionPaperViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin, 
                        mixins.UpdateModelMixin, 
                        mixins.DestroyModelMixin, 
                        viewsets.GenericViewSet
    ):

    queryset = QuestionPaper.objects.all()
    serializer_class = QuestionPaperSerializer
