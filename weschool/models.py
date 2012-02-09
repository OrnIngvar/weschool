from django.db import models

class Exam(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    course = models.ForeignKey('Course')
#    question = models.ForeignKey('Question')

    def __unicode__(self):
        return self.title

class Question(models.Model):
#    content = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    correct = models.BooleanField()
    exam = models.ForeignKey('Exam')

    def __unicode__(self):
        return self.answer

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    course = models.ForeignKey('Course')

    def __unicode__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    course = models.ForeignKey('Course')

    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name