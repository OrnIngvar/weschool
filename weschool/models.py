from django.db import models

# Create your models here.
class Exam(models.Model):
    question = models.CharField(max_length=100)