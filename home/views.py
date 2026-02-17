from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from home.models import School

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
