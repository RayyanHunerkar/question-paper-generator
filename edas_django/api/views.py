import csv
import io
from docx import Document
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.http import StreamingHttpResponse
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets
from rawquestion.models import RawQuestion
from questiongenerator.models import QuestionPaper, QuestionSet, Question
from .serializers import RawQuestionSerializer, QuestionPaperSerializer, QuestionSetSerializer, QuestionSerializer

fs = FileSystemStorage(location='tmp/')

class RawQuestionViewSet(viewsets.GenericViewSet,
                mixins.RetrieveModelMixin,
                mixins.ListModelMixin
    ):
    queryset = RawQuestion.objects.all()
    serializer_class = RawQuestionSerializer

    def create(self, request):
        try:
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
            
        except Exception as e:
            return Response({"status": "error", "message": str(e)})
class QuestionPaperViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet
    ):

    queryset = QuestionPaper.objects.all()
    serializer_class = QuestionPaperSerializer
class QuestionSetViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet
    ):

    queryset = QuestionSet.objects.all()
    serializer_class = QuestionSetSerializer
class QuestionViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin, 
                        mixins.RetrieveModelMixin,           
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet
    ):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
class ExportDocViewSet(viewsets.GenericViewSet):
    
    questionsetqueryset = QuestionSet.objects.all()
    questionqueryset = Question.objects.all()

    def list(self, *args, **kwargs):
        return Response({"status": "success"})

    def retrieve(self,request,pk, *args, **kwargs):
        
        try:
            questionpaper = QuestionPaper.objects.all().filter(QuestionPaperID=pk)
            questionset =  QuestionSet.objects.all().filter(questionpaper_id = pk)
            question = Question.objects.all().filter(questionset=questionset)
            document = Document()

            document.add_heading('Question Paper {}'.format(questionpaper.first().QuestionPaperID), 0)
            document.add_paragraph('Academic Year: {}'.format(questionpaper.first().AcademicYear))
            document.add_paragraph('Time : {}'.format(questionpaper.first().time))
            document.add_paragraph('Semester : {}'.format(questionpaper.first().semester))
            document.add_paragraph('Course: {}'.format(questionpaper.first().subjectcode.name))
            document.add_paragraph('Notes: {}'.format(questionpaper.first().exam_note.note))
            document.add_paragraph('Total Marks: {}'.format(questionpaper.first().maxmarks))
            
            for questionset in self.questionsetqueryset.all().filter(questionpaper_id = pk):
                document.add_paragraph('Question Set: {}'.format(questionset.setType))
                for question in self.questionqueryset.all():
                        if question.questionset == questionset:
                            document.add_paragraph('    Question: {}'.format(question.content))

            buffer = io.BytesIO()
            document.save(buffer)
            buffer.seek(0)

            response = StreamingHttpResponse(
                streaming_content=buffer,
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )

            response['Content-Disposition'] = 'attachment; filename=Question Paper {}.docx'.format(questionpaper.first().QuestionPaperID)
            response['Content-Encoding'] = 'utf-8'
            return response

        except Exception as e:
            return Response({"status": "error", "message": str(e)})
