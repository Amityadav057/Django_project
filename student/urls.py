from django.urls import path

from student.views import student_list, create_student, grade_view
urlpatterns = [
    path('', student_list, name="student-list"),
    path('create', create_student, name="student-create"),
    path('grade', grade_view, name="grade-view"),
    
]