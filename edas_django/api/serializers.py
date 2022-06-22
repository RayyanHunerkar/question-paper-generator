from rest_framework import serializers
from rawquestion.models import RawQuestion
from questiongenerator.models import *

class RawQuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RawQuestion
        fields = ('rawquestionID', 'content', 'difficulty', 'unit')

class QuestionSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Question
        fields = '__all__'

class QuestionSetSerializer(serializers.ModelSerializer):
        
        question = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        class Meta:
            model = QuestionSet
            fields = '__all__'
            
class AcademicYearSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AcademicYear
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exam
        fields = '__all__'

class ExamNoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExamNote
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = '__all__'

class QuestionTypeDescriptorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionTypeDescriptor
        fields = '__all__'

class SemesterDescriptorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SemesterDescriptor
        fields = '__all__'

class QuestionPaperSerializer(serializers.ModelSerializer):
    questionset = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    AcademicYear = AcademicYearSerializer()
    subjectcode = SubjectSerializer()


    class Meta:
        model = QuestionPaper
        fields = ['QuestionPaperID','maxmarks','time','exam_note','subjectcode','AcademicYear','coursename','semester','questionset']
        


class QuestionPaperSetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionPaperSet
        fields = '__all__'
