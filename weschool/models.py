from django.db import models

class Exam(models.Model):
    question = models.CharField(max_length=100)

    def __unicode__(self):
        return self.question

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey('Course')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __unicode__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name