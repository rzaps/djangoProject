from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

def new(request):
    return HttpResponse("second page")

def data(request):
    return HttpResponse("data")

def test(request):
    return HttpResponse("test")