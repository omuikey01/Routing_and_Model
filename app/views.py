from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import IndexForm



def homepage(request):
    return render(request, "index.html")


def colorname(request):
    return render(request, "color.html")

def citypage(request):
    return render(request, "city.html")

def phonepage(request):
    return render(request, "phone.html")

def moviepage(request):
    return render(request, "movie.html")

def indexformpage(request):
    name = request.GET['fname']
    email = request.GET['email']
    IndexForm.objects.create(
        person_name = name,
        person_email = email
    )
    return HttpResponse("Done!!")