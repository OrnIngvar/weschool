from models import Exam, Course, Student, Teacher, Question
from models import Question
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Question
    extra = 3


class ExamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['course', 'title']}),
        ('Date information', {'fields': ['start_date', 'end_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('course', 'title', 'start_date', 'end_date')
    list_filter = ['start_date']
    search_fields = ['question']
    date_hierarchy = 'start_date'


class CourseAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Exam, ExamAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Question)