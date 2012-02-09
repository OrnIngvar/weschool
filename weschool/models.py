from django.db import models
from django.contrib.auth.models import User

class Exam(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    course = models.ForeignKey('Course')

    def __unicode__(self):
        return self.title


class Score(models.Model):
    student = models.ForeignKey(User)
    score = models.DecimalField(decimal_places=2, max_digits=4)
    exam = models.ForeignKey('Exam')


class Question(models.Model):
    question = models.CharField(max_length=200)
    exam = models.ForeignKey('Exam')

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    answer = models.CharField(max_length=200)
    correct = models.BooleanField()
    question = models.ForeignKey('Question')


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User)

    def __unicode__(self):
        return self.name