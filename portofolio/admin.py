from django.contrib import admin

# Register your models here.
from .models import Project, Tag, Gallery, Contact, Subscriber

myModels = [Project, Tag, Gallery, Contact, Subscriber]
admin.site.register(myModels)