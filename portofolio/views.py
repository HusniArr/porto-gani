from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project, Gallery

# Create your views here.
def index(request):
    template = loader.get_template("home/index.html")
    galleries = Gallery.objects.all()
    context = {
        "title" : "Home Page",
        "galleries": galleries
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template("home/index.html")
    galleries = Gallery.objects.all()
    context = {
        "title" : "Home Page",
        "galleries": galleries
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template("about/index.html")
    galleries = Gallery.objects.all()
    context = {
        "title" : "About Page",
        "galleries": galleries
    }
    return HttpResponse(template.render(context, request))

def service(request):
    template = loader.get_template("service/index.html")
    galleries = Gallery.objects.all()
    context = {
        "title" : "Service Page",
        "galleries": galleries
    }
    return HttpResponse(template.render(context, request))

def project(request):
    template = loader.get_template("project/index.html")
    results = Project.objects.select_related("tag")
    galleries = Gallery.objects.all()
    context = {
        "title" : "Project Page",
        "results":results,
        "galleries": galleries
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template("contact/index.html")
    galleries = Gallery.objects.all()
    context = {
        "title" : "Contact Page",
        "galleries": galleries
    }
    return HttpResponse(template.render(context, request))


