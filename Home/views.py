from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req , 'Home/home.html' ,{"page" : "home"})

def about(req):
    return render(req , "Home/about-us.html" , {"page" : "about-us"})

def contact(req):
    return render(req , "Home/contact-us.html" , {"page" : "contact-us"})