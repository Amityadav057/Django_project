from django.contrib import admin
from student.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display =['name','student_id','number','school']
    list_filter = []
    search_fields = ['name']