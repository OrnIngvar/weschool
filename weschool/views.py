from django.shortcuts import render_to_response
from weschool.models import Course, Exam
from django.http import Http404

def index(request):
    course_list = Course.objects.all()
    return render_to_response('course_index.html', {'course_list': course_list})

def detail(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        p = Exam.objects.filter(course=course_id)
    except Course.DoesNotExist:
        raise Http404
    return render_to_response('course_detail.html', {'exams': p, 'course' : course})

def action(request, exam_id):
    try:
        exam = Exam.objects.get(id=exam_id)
    except Course.DoesNotExist:
        raise Http404
    return render_to_response('exam_action.htm', {'exam': exam })