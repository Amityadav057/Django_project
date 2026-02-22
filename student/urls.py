from django.urls import path

from student.views import student_list, create_student


urlpatterns = [
    path('', student_list, name="student-list"),
    path('create', create_student, name="student-create"),

]