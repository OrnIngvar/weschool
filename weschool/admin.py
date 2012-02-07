from models import Exam, Course, Student, Teacher, Question
from models import Question
from django.contrib import admin

class ExamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['course','title','question']}),
        ('Date information', {'fields': ['start_date', 'end_date']}),
    ]

class CourseAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Exam, ExamAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Question)