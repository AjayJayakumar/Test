from django.urls import path
from .views import *

urlpatterns = [
  path("new-user-login",NewUserAPIView.as_view()),
  path("text-snippet/add",AddingNewTextSnippet.as_view()),
]