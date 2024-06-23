from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# def layout(request):
#   template = loader.get_template('layout.html')
#   return HttpResponse(template.render())

def layout(request):
  return render(request, "layout.html" )

def index(request):
    return HttpResponse("Hello this is my website")

def students(req):
    
    return render(req , 'students.html' , {
        "students":[
            'royal' , 'rohan' , 'rexon'
        ]
    })