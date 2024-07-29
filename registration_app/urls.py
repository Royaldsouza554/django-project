from django.urls import path
from .views import course_details , course_list

urlpatterns =[
      path("" ,course_list , name="course_list" ),
      path("<int:course_id>/" ,course_details , name="course_details" ),
]