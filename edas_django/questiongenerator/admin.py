from django.contrib import admin
from .models import *

admin.site.register(QuestionSet)
admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(ExamNote)
admin.site.register(AcademicYear)
admin.site.register(QuestionTypeDescriptor)
admin.site.register(QuestionPaper)
admin.site.register(QuestionPaperSet)

# Register your models here.
