from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from home.models import School
from home.forms import SchoolForm

# Create your views here.
def home(request):
    print("home func")
    return HttpResponse("Hello this is from home func")


def test_views(request):
    return JsonResponse({
        "name":"test",
        "address":"nepal"
    },safe=False)


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

