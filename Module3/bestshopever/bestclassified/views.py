from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("I'm OK, I'm not alcoholic")

def about(request):
    return HttpResponse("We live on Earth")
