from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def show_time(request):
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%B-%d, %H:%M") #to get year month day hour and sec
    #formatted_time=(now.strftime("%B")) to get only month 
    return HttpResponse(f"<h2>Hello World Time Is!</h2><p>Current Time: {formatted_time}</p>")
