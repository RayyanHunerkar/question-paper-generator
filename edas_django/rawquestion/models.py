from django.db import models

class RawQuestion(models.Model):
    rawquestionID = models.AutoField(primary_key=True)
    content = models.TextField(max_length=256)
    difficulty = models.TextField(max_length=256)
    unit = models.IntegerField()



    

    
