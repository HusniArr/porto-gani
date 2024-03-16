from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project

# Create your views here.
def index(request):
    template = loader.get_template("home/index.html")
    context = {
        "title" : "Home Page"
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template("home/index.html")
    context = {
        "title" : "Home Page"
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template("about/index.html")
    context = {
        "title" : "About Page"
    }
    return HttpResponse(template.render(context, request))

def service(request):
    template = loader.get_template("service/index.html")
    context = {
        "title" : "Service Page"
    }
    return HttpResponse(template.render(context, request))

def project(request):
    template = loader.get_template("project/index.html")
    results = Project.objects.select_related("tag")
    context = {
        "title" : "Project Page",
        "results":results
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template("contact/index.html")
    context = {
        "title" : "Contact Page"
    }
    return HttpResponse(template.render(context, request))


