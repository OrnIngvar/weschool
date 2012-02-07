from django.db import models

class Exam(models.Model):
    title = models.CharField(max_length=200)
    question = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __unicode__(self):
        return self.title

class Question(models.Model):
    content = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    correct = models.BooleanField()

    def __unicode__(self):
        return self.content

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    course = models.ForeignKey('Course')

    def __unicode__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name