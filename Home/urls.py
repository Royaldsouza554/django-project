from django.urls import path

from . import views

urlpatterns = [
    path('' , views.home),
    path('about-us/' , views.about),
    path('contact-us/' , views.contact)
]