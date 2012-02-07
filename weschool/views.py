from django.shortcuts import render_to_response
from weschool.models import Course, Exam
from django.http import Http404

def index(request):
    course_list = Course.objects.all()
    return render_to_response('index.html', {'course_list': course_list})

def detail(request, course_id):
    try:
        p = Exam.objects.filter(course=course_id)
    except Course.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'exams': p})