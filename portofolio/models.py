from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    
class Project(models.Model):
    project_name = models.CharField(max_length=300)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(null=True,blank=True)
    

    