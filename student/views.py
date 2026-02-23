from django.shortcuts import render, redirect

from student.models import Student, Grade, Subject
from student.forms import StudentForm
from .forms import GradeForm
from .forms import SubjectForm
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



def grade_view(request):
    grade = Grade.objects.all()
    context = {
        "grade":grade
    }
    return render(request, 'grade/index.html', context)

# CREATE VIEW
def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade-view')
    else:
        form = GradeForm()

    return render(request, 'grade/create.html', {'form': form})


def subject_view(request):
    subjects = Subject.objects.all()
    context = {
        "subjects":subjects
    }
    return render(request, 'subject/index.html', context)

# SUBJECT CREATE
def create_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject-view')
    else:
        form = SubjectForm()

    return render(request, 'subject/create.html', {'form': form})


# grade crud operation
# grade stats