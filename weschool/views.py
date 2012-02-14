from django.contrib.auth.models import User
from django.contrib.formtools.wizard import FormWizard
from django.shortcuts import render_to_response
from django.utils.datetime_safe import date
from weschool.models import Course, Exam, Choice, Question
from django.http import Http404
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.forms.widgets import RadioSelect
from django import forms
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index(request):
    course_list = Course.objects.all()
    return render_to_response('course_index.html', {'course_list': course_list}, RequestContext(request))

def detail(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        exams = course.exam_set.filter(end_date__gte = date.today())
    except Course.DoesNotExist:
        raise Http404
    return render_to_response('course_detail.html', {'exams': exams, 'course' : course}, RequestContext(request))

def action(request, exam_id):
    if request.method == 'POST': # If the form has been submitted...
        form_data = request.POST
        exam = Exam.objects.get(id=exam_id)
        questions = exam.question_set.all()
        for question in questions:
            answer = Choice.objects.get(id=form_data['question_'+str(question.id)])
            if answer.correct:
                print "correct"
            else:
                print "false"
        return HttpResponseRedirect('results.html') # Redirect after POST
    else:
        try:
            exam = Exam.objects.get(id=exam_id)
            questions = exam.question_set.all()
            questions_list = []
            for question in questions:
                questions_list.append((question, question.choice_set.all()))
                question_length = len(questions_list)
            #form = QuestionsForm(questions_list)
#            paginator = Paginator((questions_list), 5)
#            try:
#                page = int(request.GET.get('page', '1'))
#            except ValueError:
#                page = 1
#            try:
#                p_questions_list = paginator.page(page)
#            except (EmptyPage, InvalidPage):
#                p_questions_list  = paginator.page(paginator.num_pages)

        except Course.DoesNotExist:
            raise Http404

        print questions_list

    return render_to_response('exam_action.html',
            {'questions_list' : questions_list,
             'question_length' : question_length,
             'exam': exam },
        RequestContext(request))

def home_index(request):
    return render_to_response('home.html', {'next': request}, RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def result(request, exam_id):
    return render_to_response('results.html', RequestContext(request))

class QuestionsForm(forms.Form):
    def __init__(self,questions_list, *args, **kwargs):
        super(QuestionsForm, self).__init__(*args, **kwargs)
        for question, choice_list in questions_list:
            self.fields['question_'+ str(question.id)] = forms.ChoiceField(widget=RadioSelect, label=question.question,
                choices=[(choice.id, choice.answer) for choice in choice_list])