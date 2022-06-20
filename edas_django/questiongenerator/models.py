from django.db import models
import datetime

# Create your models here.
class AcademicYear(models.Model):
    academicyearID = models.AutoField(primary_key=True)
    startDate = models.DateField()
    endDate = models.DateField()

    def year_range(self):
        return str(self.startDate.year) + "-" + str(self.endDate.year)
    

class Course(models.Model):
    courseID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

class Exam(models.Model):
    examID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    course = models.OneToOneField(Course, on_delete=models.CASCADE, null=True)

class ExamNote(models.Model):
    examnoteID = models.AutoField(primary_key=True)
    note = models.TextField()

class Subject(models.Model):
    subjectID = models.AutoField(primary_key=True)
    subjectcode = models.CharField(max_length=256, unique=True, default="unknown")
    name = models.CharField(max_length=256)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    academicyearID = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, null=False, default= 1)

class Question(models.Model):

    EASY = 'EASY'
    MEDIUM = 'MEDIUM'
    HARD = 'HARD'
    DIFFICULTY_CHOICES = (
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    )
    questionID = models.AutoField(primary_key=True)
    content = models.TextField(max_length=256)
    difficulty = models.TextField(choices=DIFFICULTY_CHOICES, default=EASY)
    unit = models.IntegerField()
    marks = models.IntegerField(default=0)
    subjectID = models.ForeignKey(Subject, on_delete=models.CASCADE, null = True)

class QuestionSet(models.Model):

    questionSetID = models.AutoField(primary_key=True)
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE)
    min_questions = models.IntegerField(default=1, null=True)
    max_questions = models.IntegerField(default=100, null=True)
    setType = models.IntegerField()
    compulsorymarks = models.IntegerField(null=True)
    optionalmarks = models.IntegerField(null=True)

    def totalquestions(self):
        return self.min_questions + self.max_questions

    def total_marks(self):
        return self.compulsorymarks + self.optionalmarks

class QuestionPaper(models.Model):
    QuestionPaperID = models.AutoField(primary_key=True)
    maxmarks = models.IntegerField(default=100)
    time = models.TimeField(default=datetime.time(2, 30, 0))
    exam_noteID = models.ForeignKey(ExamNote, on_delete=models.CASCADE, null=True)
    subjectcode  = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    QuestionSetID = models.ForeignKey(QuestionSet, on_delete=models.CASCADE) # Should this store the setIDs as a list? 
    AcademicYearID = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, null=False, default=1)
    coursename = models.TextField(max_length=256)
    semester = models.IntegerField()
    

class QuestionPaperSet(models.Model):
    questionPaperSetID = models.AutoField(primary_key=True)
    paperSet = models.IntegerField()
    questionPaperID = models.ForeignKey(QuestionPaper, on_delete=models.CASCADE)

class QuestionTypeDescriptor(models.Model):
    quesitiontypedescriptorID = models.AutoField(primary_key=True)
    code_value = models.IntegerField()
    short_desc = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

class SemesterDescriptor(models.Model):
    semesterdescriptorID = models.AutoField(primary_key=True)
    code_value = models.IntegerField()
    short_desc = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

