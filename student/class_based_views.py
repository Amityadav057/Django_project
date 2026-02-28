from django.views.generic.list import ListView

from student.models import Student



class StudentListView(ListView):
    model = Student
    template_name = "student/index.html"
    context_object_name = "student"
