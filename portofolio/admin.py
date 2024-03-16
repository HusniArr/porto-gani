from django.contrib import admin

# Register your models here.
from .models import Project, Tag

myModels = [Project, Tag]
admin.site.register(myModels)