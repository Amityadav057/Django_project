from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from student.forms import StudentForm
from student.models import Grade, Student

# Create your views here.

@login_required()
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



def grade_view(request):
    grade = Grade.objects.all()
    context = {
        "grade":grade
    }
    return render(request, 'grade/index.html', context)


# grade crud operation
# grade stats