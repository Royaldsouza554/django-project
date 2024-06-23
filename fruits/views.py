from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fruits(req):
    
    return render(req , 'fruits.html' , {
        "fruits":[
            'apple' , 'banana' , 'mango'
        ]
    })
