from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Model for Text Snippets
class TextSnippets(models.Model):
    title = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Created Time')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)