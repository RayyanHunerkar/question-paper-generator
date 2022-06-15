from django.db import models

# Create your models here.
class Question(models.Model):
    questionID = models.AutoField(primary_key=True)
    content = models.TextField(max_length=256)
    difficulty = models.TextField(max_length=256)
    unit = models.IntegerField()

class QuestionSet(models.Model):
    questionSetID = models.AutoField(primary_key=True)
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE)
    setType = models.IntegerField()


class QuestionPaper(models.Model):
    QuestionPaperID = models.AutoField(primary_key=True)
    QuestionSetID = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
    coursename = models.TextField(max_length=256)
    semester = models.IntegerField()
