from django.db import models

class Exam(models.Model):
    question = models.CharField(max_length=100)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey('Course')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)