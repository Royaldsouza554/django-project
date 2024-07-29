from django.shortcuts import render , get_object_or_404

from .models import Student , Course

def course_list(req):
      courses = Course.objects.all()
      return render(req , "course_list.html" ,{"courses" : courses})


def course_details(req , course_id):
      course = get_object_or_404(Course , id=course_id)

      students = course.students.all()

      return render(req , "course_details.html" , {"course":course , "students":students})
