from django.db import models

# Create your models here.
class Project(models.Model):
    student_name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    language_used = models.CharField(max_length=50)
    duration = models.IntegerField(help_text="Duration in months")

    def __str__(self):
      return f"{self.student_name} - {self.topic}"