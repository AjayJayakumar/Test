from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TextSnippets
from .serializers import NewUserSerializer, TextSnippetSerializer
from django.contrib.auth.models import User
from rest_framework import generics,status




# Adding New User/ User Sign Up
class NewUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = NewUserSerializer


# Adding New text snippet
class AddingNewTextSnippet(APIView):
    def post(self,request):
        response_data = {}
        data = {
            'title': request.data.get('title'), 
            'created_user': request.data.get('created_user')
        }
        serializer = TextSnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data['status_code'] = '200'
            response_data['status'] = True
            response_data['message'] = 'Text Snippet is added successfully. '
            resp_status = status.HTTP_200_OK
        else:
            response_data['status_code'] = '400'
            response_data['status'] = False
            response_data['message'] = 'Invalid Data, Text Snippet is not added'
            resp_status = status.HTTP_400_BAD_REQUEST

        return Response(response_data, status=resp_status)
       
       
       