from django.shortcuts import render_to_response
from weschool.models import Course, Exam, Choice, Question
from django.http import Http404
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

def index(request):
    if request.user.is_authenticated():
        course_list = Course.objects.all()
        return render_to_response('course_index.html', {'course_list': course_list, 'user': request.user})
    else:
        return render_to_response('login.html')


def detail(request, course_id):
    if request.user.is_authenticated():
        try:
            course = Course.objects.get(id=course_id)
            exams = course.exam_set.all()
        except Course.DoesNotExist:
            raise Http404
        return render_to_response('course_detail.html', {'exams': exams, 'course' : course})
    else:
        return render_to_response('login.html')

def action(request, exam_id):
    if request.user.is_authenticated():
        try:
            exam = Exam.objects.get(id=exam_id)
            questions = exam.question_set.all()
            questions_list = []
            for question in questions:
                questions_list.append((question, question.choice_set.all()))
        except Course.DoesNotExist:
            raise Http404
        return render_to_response('exam_action.html', {'exam': exam, 'questions_list' : questions_list })
    else:
        return render_to_response('login.html')

def home_index(request):
    return render_to_response('home.html', {'next': request, 'user': request.user})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')