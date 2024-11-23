from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse("<h2>this is my first project</h2>")

def second(request):
    return HttpResponse("<h1><marquee>hai </marquee></h1>")
def third(request):
    return HttpResponse("<h1>name=jyothsna reddy<br>age=20<br>gender=female<br>nativeplace=badvel</h1>") 
def four(request):
    return HttpResponse("<h1><i>i dont like to read my books again ;i want to move to a new chapter</i>")   
def five(request):
    return HttpRespons("<i>hai</i>")