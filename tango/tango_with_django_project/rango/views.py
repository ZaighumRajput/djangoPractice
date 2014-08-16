from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world!")

def about(request):
    return HttpResponse("Rango says: Hello world! <a href='/rango/about'>About</a><a href='/rango/'>Index</a>")
# Create your views here.
