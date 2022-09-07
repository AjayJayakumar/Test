from django.urls import path
from .views import *
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('text-snippet/get',views.GetTextSnippetViewset, basename='provider-suspence-account')


urlpatterns = [
  path("new-user-login",NewUserAPIView.as_view()),
  path("text-snippet/add",AddingNewTextSnippet.as_view()),
  path("text-snippet/get/<int:pk>/",GetTextSnippet.as_view()),
  path("text-snippet/update/",UpdatingTextSnippet.as_view()),
]

urlpatterns += router.urls
