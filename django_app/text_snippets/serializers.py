from rest_framework import serializers
from .models import *

class TextSnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextSnippets
        fields = ('id','title','created_time','created_by')
        