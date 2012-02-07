from django.shortcuts import render_to_response
from weschool.models import Exam

def index(request):
    exams_list = Exam.objects.all()
    return render_to_response('index.html', {'exams_list': exams_list})