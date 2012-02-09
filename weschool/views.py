from django.shortcuts import render_to_response
from weschool.models import Course, Exam, Choice, Question
from django.http import Http404

def index(request):
    course_list = Course.objects.all()
    return render_to_response('course_index.html', {'course_list': course_list})

def detail(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        exams = course.exam_set.all()
    except Course.DoesNotExist:
        raise Http404
    return render_to_response('course_detail.html', {'exams': exams, 'course' : course})

def action(request, exam_id):
    try:
        exam = Exam.objects.get(id=exam_id)
        questions = exam.question_set.all()
        questions_list = []
        for question in questions:
            questions_list.append((question, question.choice_set.all()))
    except Course.DoesNotExist:
        raise Http404
    return render_to_response('exam_action.html', {'exam': exam, 'questions_list' : questions_list })