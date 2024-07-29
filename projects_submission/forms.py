
from django import forms
from .models import Project

class StudentForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["student_name" , "topic" , "language_used" , "duration"]
