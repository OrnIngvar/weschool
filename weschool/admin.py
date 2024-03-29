from models import Exam, Course, Question, Choice
from models import Question
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

class ChoiceInline(admin.TabularInline):
    model = Choice
#    extra = 3


class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 3


class ExamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['course', 'title']}),
        ('Date information', {'fields': ['start_date', 'end_date']}),
    ]
    inlines = [QuestionInLine]
    list_display = ('course', 'title', 'start_date', 'end_date')
    list_filter = ['start_date']
    search_fields = ['question']
    date_hierarchy = 'start_date'


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question','exam']}),
    ]
    inlines = [ChoiceInline]


class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'teacher']


admin.site.register(Exam, ExamAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

#Unregister auth and sites from admin view
#admin.site.unregister(User)
#admin.site.unregister(Group)
#admin.site.unregister(Site)