from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def layout(request):
  return render(request, "layout.html" )

def students(req):
    
    return render(req , 'students.html' , {
        "students":[
            'royal' , 'rohan' , 'rexon'
        ]
    })