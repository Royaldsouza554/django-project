from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req , 'Home/home.html')

def about(req):
    return render(req , "Home/about-us.html")

def contact(req):
    return render(req , "Home/contact-us.html")