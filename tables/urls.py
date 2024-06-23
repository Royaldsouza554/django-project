from django.urls import path
from . import views

urlpatterns = [
    path('<int:number>/<int:count>/', views.table, name='table'),
]
