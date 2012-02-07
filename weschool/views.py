from django.shortcuts import render_to_response
from weschool.models import Course

def index(request):
    exams_list = Course.objects.all()
    return render_to_response('index.html', {'exams_list': exams_list})