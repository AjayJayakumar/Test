from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TextSnippets
from .serializers import NewUserSerializer, TextSnippetSerializer
from django.contrib.auth.models import User
from rest_framework import generics,status,viewsets




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
            'created_by': request.data.get('created_user')
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
       

# Get Text Snippet Details           
class GetTextSnippet(APIView):
    
    def get(self,request,pk):
        response_data = {}
        data = {}
        data_to_view = TextSnippets.objects.filter(id=pk)
        print(data_to_view)
        if data_to_view:
            retrieved_data = {
            'title': data_to_view.values_list('title'), 
            'created_time': data_to_view.values_list('created_time'),
            'created_user': data_to_view.values_list('created_by_id')
            }

            data = retrieved_data
            if data:
                response_data['status_code'] = '200'
                response_data['status'] = True
                response_data['message'] = 'Text Snippet Details fetched. '
                response_data['data'] = data
                resp_status = status.HTTP_200_OK
            else:
                response_data['status_code'] = '400'
                response_data['status'] = False
                response_data['message'] = 'Text Snippet Details not fetched.'
                resp_status = status.HTTP_400_BAD_REQUEST

        return Response(response_data, status=resp_status)


