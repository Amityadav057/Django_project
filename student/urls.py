from django.urls import path

from student.views import create_grade, student_list, create_student, grade_view, subject_view, create_subject
urlpatterns = [
    path('', student_list, name="student-list"),
    path('create', create_student, name="student-create"),
    path('grade', grade_view, name="grade-view"),
     path('create/',create_grade, name='create-grade'),
     path('subject', subject_view, name="subject-view"),
     path('subject/create/', create_subject, name='create-subject'),
    
]