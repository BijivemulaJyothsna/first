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
    return HttpResponse("""
    <h1>Dhoni</h1>
    <img 
    src="https://www.google.com/url?sa=i&url=https%3A%2F%2Ftimesofindia.indiatimes.com%2Fsports%2Fcricket%2Fipl%2Ftop-stories%2Fipl-2024-ms-dhoni-becomes-first-player-to-make-this-big-record-in-chennai-super-kings-win-against-sunrisers-hyderabad%2Farticleshow%2F109675316.cms&psig=AOvVaw3yTFPBTuFD4TmpcocK5ek4&ust=1732298707541000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCID84qmC7okDFQAAAAAdAAAAABAh.jpg alt="dhoni image">
    """)