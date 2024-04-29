from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project, Gallery, Contact
from .forms import ContactForm
from django.shortcuts import redirect, render
from django.utils import timezone

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

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
        
            contact = Contact.objects.create(
                full_name = full_name,
                email = email,
                subject = subject,
                message = message
            )
            contact.save()
            return redirect('/contact')
    else:
        form = ContactForm()
        return render(request, 'contact/index.html', {'form': form, 'title':  'Contact Page'})
