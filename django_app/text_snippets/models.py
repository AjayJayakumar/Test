from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Model for Tag
class Tag(models.Model):
    tag = models.CharField(max_length=100)

# Model for Text Snippets
class TextSnippets(models.Model):
    title = models.ForeignKey(Tag, on_delete=models.CASCADE,null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Created Time')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    is_deleted = models.BooleanField(default=False)