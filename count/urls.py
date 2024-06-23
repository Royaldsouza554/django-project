from django.urls import path
from . import views

urlpatterns = [
    path('<str:sentence>/', views.count_letters, name='count_letters'),
]
