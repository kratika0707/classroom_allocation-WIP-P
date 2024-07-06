from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import timetable
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q





# Create your views here.
def search(request):
    if request.method=="POST":
        searchyear=request.POST.get('year')
        searchcourse=request.POST.get('course')
        ttsearch=timetable.objects.filter(year=searchyear,course=searchcourse)
        return render(request,'search.html',{"data":ttsearch})
    else :
        
        return render(request,'search.html')