from django.contrib import admin
from student.models import Student, Subject, Grade

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =['name','student_id','number','school']
    list_filter = []
    search_fields = ['name']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display =['name','created_at','updated_at']
    list_filter = []
    search_fields = ['name']


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display =['name','created_at','updated_at']
    autocomplete_fields = ['subject']
    list_filter = []
    search_fields = ['name']

