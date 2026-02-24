from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from home.models import School
from home.forms import SchoolForm
from student.models import Student
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def home(request):
    school_status = School.objects.values('is_active').annotate(count = Count('is_active'))
    school_student_count = Student.objects.values('school__name').annotate(count = Count('id')).order_by('-count')
    last_five_school = School.objects.filter(is_active = True).order_by('-updated_at')[:5]
    context = {
        "student_count":Student.objects.all().count(),
        "school_count":School.objects.all().count(),
        "school_status":school_status,
        "last_five_school":last_five_school,
        "school_student_count":school_student_count
    }
    return render(request, 'base/base.html', context)


def test_views(request):
    return JsonResponse({
        "name":"test",
        "address":"nepal"
    },safe=False)

@login_required()
def school_list(request):
    school = School.objects.all()
    return render(request, 'school/school.html', {"school":school})


def school_create(request):
    if request.method == "POST":
        data = request.POST
        School.objects.create(
            name = data['name'],
            school_unique_code = data['unique_code'],
            address = data['address'],
        )
        return redirect('/home/school')
    return render(request, 'school/create.html')


def school_create2(request):
    if request.method == "POST":
        data = request.POST
        form = SchoolForm(data=data)
        if form.is_valid():
            form.save()
            return redirect('/home/school')
        else:
            return render(request, 'school/create2.html',{'form':form})
    else:
        form = SchoolForm()


    return render(request, 'school/create2.html',{'form':form})



def school_update(request,id):
    school = School.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        form = SchoolForm(data=data, instance=school)
        if form.is_valid():
            form.save()
            return redirect('/home/school')
        else:
            return render(request, 'school/update.html',{'form':form})
    else:
        form = SchoolForm(instance=school)


    return render(request, 'school/update.html',{'form':form})


def delete_school(request,id):
    school = School.objects.filter(id=id)
    school.delete()
    return redirect('/home/school')

