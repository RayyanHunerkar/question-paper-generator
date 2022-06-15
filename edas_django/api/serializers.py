from rest_framework import serializers
from rawquestion.models import RawQuestion


class RawQuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RawQuestion
        fields = ('rawquestionID', 'content', 'difficulty', 'unit')