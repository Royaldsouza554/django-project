from django.urls import path

from . import views

urlpatterns = [
    path("", views.date, name="date"),
    path('<int:offset>/' , views.dateWithOffset )
]