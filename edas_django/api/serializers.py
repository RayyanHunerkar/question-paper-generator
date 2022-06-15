from rest_framework import serializers
from rawquestion.models import rawquestion


class RawQuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = rawquestion
        fields = ('rawquestionID', 'content', 'difficulty', 'unit')