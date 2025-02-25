from django.db import models

class Student(models.Model):
      first_name = models.CharField(max_length=100) 
      last_name = models.CharField(max_length=100) 

      def __str__(self):
            return f'{self.first_name} {self.last_name}'

class Course(models.Model):
      name = models.CharField(max_length=100) 
      students = models.ManyToManyField(Student , blank=True)

      def __str__(self):
            return self.name