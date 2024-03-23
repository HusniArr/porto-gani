from django.contrib import admin

# Register your models here.
from .models import Project, Tag, Gallery

myModels = [Project, Tag, Gallery]
admin.site.register(myModels)