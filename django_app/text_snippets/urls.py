from django.urls import path
from .views import *
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('text-snippet/view',views.GetAllTextSnippets, basename='get-all-text-snippets')
router.register('tag/view',views.GetAllTags, basename='get-all-tags')


urlpatterns = [
  path("new-user-login",NewUserAPIView.as_view()),
  path("tag/get/<int:pk>/",GetTag.as_view()),
  path("tag/add",AddingNewTag.as_view()),
  path("text-snippet/add",AddingNewTextSnippet.as_view()),
  path("text-snippet/get/<int:pk>/",GetTextSnippet.as_view()),
  path("text-snippet/update/",UpdatingTextSnippet.as_view()),
]

urlpatterns += router.urls
