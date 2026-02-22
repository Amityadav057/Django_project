from django.shortcuts import render, redirect

from student.models import Student
from student.forms import StudentForm
# Create your views here.
def student_list(request):
    data = Student.objects.all()
    context = {
        "student":data
    }
    return render(request, 'student/index.html', context)



def create_student(request):
    if request.method == "POST":
        data = request.POST
        form = StudentForm(data=data)
        if form.is_valid():
            form.save()
            return redirect('/student')
    else:
        form = StudentForm()


    return render(request, 'student/create.html',{'form':form})