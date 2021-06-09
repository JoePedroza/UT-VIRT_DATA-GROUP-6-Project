from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):    
    return render(request, "index.html")

def public(request):    
    return render(request, "public_page.html")

def submitted(request):    
    return render(request, "submitted.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
