from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def show_name_skills(request):
    return HttpResponse("<h2>Name: Sai Ganesh sharma </h2><p>Skills: Python, Django, Angular </p>")
